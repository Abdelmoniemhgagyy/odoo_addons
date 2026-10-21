This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
models/
  __init__.py
  approval_product_line.py
  approval_request.py
views/
  approval_product_line_views.xml
  approval_request_views.xml
__init__.py
__manifest__.py
```

# Files

## File: models/__init__.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import approval_product_line
from . import approval_request
```

## File: models/approval_product_line.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.fields import Domain


class ApprovalProductLine(models.Model):
    _inherit = 'approval.product.line'

    def _default_warehouse_id(self):
        company_id = self.env.context.get('default_company_id', self.env.company.id)
        warehouse = self.env['stock.warehouse'].search(
            [('company_id', '=', company_id)], limit=1
        )
        return warehouse

    warehouse_id = fields.Many2one('stock.warehouse', string="Warehouse",
        default=lambda self: self._default_warehouse_id(), check_company=True)

    def _get_picking_type(self):
        """ Returns the picking type for incoming picking, depending of the
        product line warehouse. """
        self.ensure_one()
        if not self.warehouse_id:
            return None
        return self.warehouse_id.in_type_id

    def _get_purchase_orders_domain(self, vendor):
        """ Override to filter purchase orders on warehouse. """
        domain = super()._get_purchase_orders_domain(vendor)
        picking_type = self._get_picking_type()
        if picking_type:
            domain &= Domain('picking_type_id', '=', picking_type.id)
        return domain

    def _get_purchase_order_values(self, vendor):
        vals = super()._get_purchase_order_values(vendor)
        picking_type = self._get_picking_type()
        if picking_type:
            vals['picking_type_id'] = picking_type.id
        return vals
```

## File: models/approval_request.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    hide_location = fields.Boolean(compute='_compute_hide_location')

    @api.depends('approval_type', 'has_location')
    def _compute_hide_location(self):
        multi_warehouse = self.env.user.has_group('stock.group_stock_multi_warehouses')
        for request in self:
            request.hide_location = (
                request.has_location == 'no' or (multi_warehouse and request.approval_type == 'purchase')
            )
```

## File: views/approval_product_line_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="approval_purchase_stock_product_line_view_tree_inherit" model="ir.ui.view">
        <field name="name">approval.purchase.stock.product.line.view.list.inherit</field>
        <field name="model">approval.product.line</field>
        <field name="inherit_id" ref="approvals.approval_product_line_view_tree"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='description']" position="after">
                <field name="warehouse_id" groups="stock.group_stock_multi_warehouses"
                    options="{'no_create_edit': True, 'no_open': True}"
                    column_invisible="parent.has_location == 'no'"
                    required="parent.has_location == 'required'"/>
            </xpath>
        </field>
    </record>

    <record id="approval_purchase_stock_product_line_view_form_inherit" model="ir.ui.view">
        <field name="name">approval.purchase.stock.product.line.view.form.inherit</field>
        <field name="model">approval.product.line</field>
        <field name="inherit_id" ref="approvals.approval_product_line_view_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='description']" position="after">
                <field name="warehouse_id" groups="stock.group_stock_multi_warehouses"/>
            </xpath>
        </field>
    </record>
</odoo>
```

## File: views/approval_request_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="approval_purchase_stock_request_view_form_inherit" model="ir.ui.view">
        <field name="name">approval.purchase.stock.request.view.form.inherit</field>
        <field name="model">approval.request</field>
        <field name="inherit_id" ref="approvals.approval_request_view_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='product_line_ids']" position="attributes">
                <attribute name="context">{
                    'list_view_ref': 'approvals.approval_product_line_view_tree',
                    'default_company_id': company_id,
                }</attribute>
            </xpath>
            <xpath expr="//field[@name='location']" position="before">
                <field name="hide_location" invisible="1"/>
            </xpath>
            <xpath expr="//field[@name='location']" position="attributes">
                <attribute name="invisible">hide_location</attribute>
                <attribute name="required">has_location == 'required' and approval_type != 'purchase'</attribute>
            </xpath>
        </field>
    </record>
</odoo>
```

## File: __init__.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models
```

## File: __manifest__.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Approvals - Purchase - Stock',
    'version': '1.0',
    'category': 'Human Resources/Approvals',
    'description': """ Technical module to link Approvals, Purchase and Inventory together. """,
    'depends': ['approvals_purchase', 'purchase_stock'],
    'data': [
        'views/approval_product_line_views.xml',
        'views/approval_request_views.xml',
    ],
    'installable': True,
    'auto_install': True,
    'author': 'Odoo S.A.',
    'license': 'OEEL-1',
}
```
