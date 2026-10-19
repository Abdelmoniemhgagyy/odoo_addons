# -*- coding: utf-8 -*-
from odoo import api, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import formatLang

class ReportListView(models.AbstractModel):
    _name = 'report.asl_list_view_pdf_print.report_list_view'
    _description = 'List View PDF Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if not data or not data.get('model'):
            raise UserError(_("No data provided to generate the report."))

        res_model = data.get('model')
        domain = data.get('domain', [])
        field_configs = data.get('fields', []) 
        groupby = data.get('groupby', [])
        title = data.get('title', _('List View Export'))
        res_ids = data.get('res_ids', [])

        Model = self.env[res_model]
        
        if not Model.has_access('read'):
            raise UserError(_("You do not have permission to read records from %s", res_model))

        # Use Model Name (e.g. Sales Order) instead of technical name (sale.order)
        title = data.get('title')
        if not title or title == res_model:
            title = Model._description

        headers = [f['label'] for f in field_configs]
        field_names = [f['name'] for f in field_configs]
        fields_info = Model.fields_get(field_names, ['type'])

        # Prepare aggregate fields for _read_group/formatted_read_group
        aggregates = []
        for f in field_configs:
            f_name = f['name']
            f_type = fields_info.get(f_name, {}).get('type')
            if f.get('aggregate'):
                aggregates.append(f"{f_name}:{f['aggregate']}")
            elif f_type in ['float', 'monetary', 'integer']:
                # Auto-sum for numeric fields as requested by user
                aggregates.append(f"{f_name}:sum")

        rows = []
        if groupby:
            # Grouped Export Logic
            domain_to_use = [('id', 'in', res_ids)] if res_ids else domain
            rows = self._get_grouped_rows(Model, domain_to_use, field_names, fields_info, groupby, aggregates, field_configs)
        else:
            # Flat Export Logic
            records = Model.browse(res_ids).exists() if res_ids else Model.search(domain)
            export_result = records.with_context(import_compat=False).export_data(field_names)
            raw_rows = export_result.get('datas', [])
            for raw_row in raw_rows:
                rows.append({'type': 'data', 'values': self._format_row(raw_row, field_names, fields_info)})

        # Calculate Grand Totals
        grand_totals = []
        has_totals = False
        if aggregates:
            total_domain = [('id', 'in', res_ids)] if res_ids else domain
            total_data = Model._read_group(total_domain, aggregates=aggregates)
            if total_data:
                res_values = total_data[0]
                # Map tuple values back to field names for compatibility
                res = {agg.split(':')[0]: val for agg, val in zip(aggregates, res_values)}
                grand_totals.append(_("Total")) # Label for first column
                for i in range(1, len(field_names)):
                    f_name = field_names[i]
                    val = res.get(f_name)
                    # Check if this field is in our aggregates list (even if value is 0)
                    is_aggregated = any(a.startswith(f"{f_name}:") for a in aggregates)
                    if val is not None and is_aggregated:
                        grand_totals.append(self._format_value(val, f_name, fields_info))
                        has_totals = True
                    else:
                        grand_totals.append('')
        
        return {
            'doc_ids': docids,
            'doc_model': res_model,
            'headers': headers,
            'rows': rows,
            'title': title,
            'grand_totals': grand_totals if has_totals else None,
        }

    def _get_grouped_rows(self, Model, domain, field_names, fields_info, groupby, aggregates, field_configs, depth=0):
        rows = []
        if not groupby:
            # Reach the leaf, fetch records
            records = Model.search(domain)
            export_result = records.with_context(import_compat=False).export_data(field_names)
            for raw_row in export_result.get('datas', []):
                rows.append({'type': 'data', 'values': self._format_row(raw_row, field_names, fields_info)})
            return rows

        current_groupby = groupby[0]
        # formatted_read_group to get sub-groups with domains
        fields_to_read = ['__count'] + aggregates
        groups_data = Model.formatted_read_group(domain, [current_groupby], fields_to_read)
        
        for group in groups_data:
            # For compatibility, map 'field:agg' to 'field'
            for agg_spec in fields_to_read:
                if agg_spec in group:
                    group[agg_spec.split(':')[0]] = group[agg_spec]

            # Build group header
            group_name = self._format_group_name(Model, current_groupby, group)
            count = group.get('__count') or 0
            header_label = f"{'    ' * depth}{group_name} ({count})"
            
            # Group headers show aggregates in their respective columns
            header_values = [header_label]
            for i in range(1, len(field_names)):
                f_name = field_names[i]
                val = group.get(f_name)
                is_aggregated = any(a.startswith(f"{f_name}:") for a in aggregates)
                if val is not None and is_aggregated:
                    header_values.append(self._format_value(val, f_name, fields_info))
                else:
                    header_values.append('')
            
            rows.append({'type': 'header', 'values': header_values, 'depth': depth})
            
            # Recursive call for children
            child_domain = group.get('__extra_domain', [])
            rows.extend(self._get_grouped_rows(Model, child_domain, field_names, fields_info, groupby[1:], aggregates, field_configs, depth + 1))
            
        return rows

    def _format_group_name(self, Model, groupby_field, group_data):
        field_name = groupby_field.split(':')[0]
        field = Model._fields.get(field_name)
        value = group_data.get(groupby_field)
        
        if value is False or value is None:
            return _("Undefined")
            
        if field.type == 'many2one':
            return value[1] if isinstance(value, (list, tuple)) else value
        elif field.type == 'selection':
            return dict(field.selection).get(value, value)
        elif field.type == 'boolean':
            return _('Yes') if value else _('No')
            
        return str(value)

    def _format_row(self, raw_row, field_names, fields_info):
        formatted_row = []
        for i, value in enumerate(raw_row):
            formatted_row.append(self._format_value(value, field_names[i], fields_info))
        return formatted_row

    def _format_value(self, value, field_name, fields_info):
        field_type = fields_info.get(field_name, {}).get('type')
        if field_type in ['float', 'monetary'] and isinstance(value, (int, float)):
            return formatLang(self.env, value)
        elif field_type == 'integer' and isinstance(value, int):
            return formatLang(self.env, value, digits=0)
        elif value is False or value is None:
            return ''
        return str(value)
