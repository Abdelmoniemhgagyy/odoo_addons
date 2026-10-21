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
data/
  approval_category_data.xml
  approval_demo.xml
  mail_templates.xml
models/
  __init__.py
  approval_category.py
  approval_product_line.py
  approval_request.py
  purchase_order.py
  res_partner.py
static/
  src/
    img/
      RFQ.png
views/
  approval_category_views.xml
  approval_product_line_views.xml
  approval_request_views.xml
__init__.py
__manifest__.py
```

# Files

## File: data/approval_category_data.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <record id="approval_category_data_rfq" model="approval.category">
            <field name="name">Create RFQ's</field>
            <field name="approval_type">purchase</field>
            <field name="image" type="base64" file="approvals_purchase/static/src/img/RFQ.png"/>
            <field name="sequence">80</field>
            <field name="has_product">required</field>
            <field name="has_quantity">required</field>
            <field name="automated_sequence" eval="True"/>
            <field name="sequence_code">APPR</field>
        </record>
    </data>
</odoo>
```

## File: data/approval_demo.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <record id="approval_category_data_rfq" model="approval.category">
            <field name="user_ids" eval="[(4, ref('base.user_admin'))]"/>
        </record>
    </data>
</odoo>
```

## File: data/mail_templates.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
<template id="exception_approval_request_canceled"
    name="Message: Alert on purchase orders when cancel an Approval Request may modify the wanted quantities.">
    <div>
        <p>
            Exception occurred: the Approval Request
            <t t-foreach="approval_requests" t-as="approval_request">
                <a href="#" data-oe-model="approval.request" t-att-data-oe-id="approval_request.id">
                    <t t-esc="approval_request.name"/>
                </a>
            </t> has been canceled.
            Manual actions may be needed.
        </p>
        <div class="mt16">
            <p>Exception(s):</p>
            <ul>
                <li t-foreach="product_lines" t-as="line">
                    <a href="#" data-oe-model="approval.request" t-att-data-oe-id="line.approval_request_id.id">
                        <t t-esc="line.approval_request_id.name"/>
                    </a>:
                    <t t-esc="line.po_uom_qty"/>
                    <t t-esc="line.product_uom_id.name"/> of
                    <t t-esc="line.product_id.name"/> cancelled
                </li>
            </ul>
        </div>
    </div>
</template>
</odoo>
```

## File: models/__init__.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import approval_category
from . import approval_product_line
from . import approval_request
from . import res_partner
from . import purchase_order
```

## File: models/approval_category.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ApprovalCategory(models.Model):
    _inherit = 'approval.category'

    approval_type = fields.Selection(selection_add=[('purchase', 'Create RFQ\'s')])

    @api.onchange('approval_type')
    def _onchange_approval_type(self):
        if self.approval_type == 'purchase':
            self.has_product = 'required'
            self.has_quantity = 'required'
```

## File: models/approval_product_line.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.fields import Domain


class ApprovalProductLine(models.Model):
    _inherit = 'approval.product.line'

    def _domain_product_id(self):
        """ Filters on product to get only the ones who are available on
        purchase in the case the approval request type is purchase. """
        # TODO: How to manage this when active model isn't approval.category ?
        if 'default_category_id' in self.env.context:
            category_id = self.env.context.get('default_category_id')
        elif self.env.context.get('active_model') == 'approval.category':
            category_id = self.env.context.get('active_id')
        else:
            return []
        category = self.env['approval.category'].browse(category_id)
        if category.approval_type == 'purchase':
            return [('purchase_ok', '=', True)]

    po_uom_qty = fields.Float(
        "Purchase Unit Quantity", compute='_compute_po_uom_qty',
        help="The quantity converted into the Unit used by the product in Purchase Order.")
    purchase_order_line_id = fields.Many2one('purchase.order.line')
    product_id = fields.Many2one(domain=lambda self: self._domain_product_id())
    product_template_id = fields.Many2one(related='product_id.product_tmpl_id')
    seller_id = fields.Many2one('product.supplierinfo', 'Vendors', compute='_compute_seller_id',
        store=True, readonly=False)
    has_no_seller = fields.Boolean(compute='_compute_has_no_seller', export_string_translation=False)

    @api.depends('approval_request_id.approval_type', 'product_uom_id', 'quantity')
    def _compute_po_uom_qty(self):
        for line in self:
            approval_type = line.approval_request_id.approval_type
            if approval_type == 'purchase' and line.product_id and line.quantity:
                uom = line.product_uom_id or line.product_id.uom_id
                line.po_uom_qty = uom._compute_quantity(
                    line.quantity,
                    line.product_id.uom_id,
                )
            else:
                line.po_uom_qty = 0.0

    @api.depends('product_id', 'po_uom_qty', 'product_id.seller_ids')
    def _compute_seller_id(self):
        for line in self:
            if line.product_id and line.po_uom_qty:
                line.seller_id = line.product_id.with_company(line.company_id)._select_seller(
                    quantity=line.po_uom_qty,
                    uom_id=line.product_id.uom_id,
                )
                if not line.seller_id:
                    # If no vendor found for the right quantity, we still want to display a vendor if any
                    line.seller_id = line.product_id.with_company(line.company_id)._select_seller(
                        quantity=None,
                        uom_id=line.product_id.uom_id,
                    )

    @api.depends('product_id', 'po_uom_qty', 'product_id.seller_ids')
    def _compute_has_no_seller(self):
        for line in self:
            line.has_no_seller = False
            if line.product_id and line.po_uom_qty:
                line.has_no_seller = not bool(line.product_id.with_company(line.company_id)._select_seller(
                    quantity=line.po_uom_qty,
                    uom_id=line.product_id.uom_id,
                ))
                if line.has_no_seller:
                    # If no vendor found for the right quantity, we still want to know if there is a vendor
                    line.has_no_seller = not bool(line.product_id.with_company(line.company_id)._select_seller(
                        quantity=None,
                        uom_id=line.product_id.uom_id,
                    ))

    def _check_products_vendor(self):
        """ Raise an error if at least one product requires a seller. """
        product_lines_without_seller = self.filtered(lambda line: line.has_no_seller)
        if product_lines_without_seller:
            product_names = product_lines_without_seller.product_id.mapped('display_name')
            raise UserError(
                _('Please select a vendor on product line or set it on product(s) %s.', ', '.join(product_names))
            )

    def _get_purchase_orders_domain(self, vendor):
        """ Return a domain to get purchase order(s) where this product line could fit in.
        """
        self.ensure_one()
        return Domain([
            ('company_id', '=', self.company_id.id),
            ('partner_id', '=', vendor.id),
            ('state', '=', 'draft'),
            ('currency_id', '=', self.seller_id.currency_id.id),
        ])

    def _get_purchase_order_values(self, vendor):
        """ Get some values used to create a purchase order.
        Called in approval.request `action_create_purchase_orders`.

        :param vendor: a res.partner record
        :return: dict of values
        """
        self.ensure_one()
        vals = {
            'origin': self.approval_request_id.name,
            'partner_id': vendor.id,
            'company_id': self.company_id.id,
            'payment_term_id': vendor.property_supplier_payment_term_id.id,
            'fiscal_position_id':self.env['account.fiscal.position']._get_fiscal_position(vendor).id,
            'currency_id': self.seller_id.currency_id.id,
        }
        return vals
```

## File: models/approval_request.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from markupsafe import Markup

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import clean_context


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    purchase_order_count = fields.Integer(compute='_compute_purchase_order_count')

    @api.depends('product_line_ids.purchase_order_line_id')
    def _compute_purchase_order_count(self):
        for request in self:
            purchases = request.product_line_ids.purchase_order_line_id.order_id
            request.purchase_order_count = len(purchases)

    def action_approve(self, approver=None):
        if self.approval_type == 'purchase' and any(not line.product_id for line in self.product_line_ids):
            raise UserError(_("You must select a product for each line of requested products."))
        return super().action_approve(approver)

    def action_cancel(self):
        """ Override to unlink the products of the cancelled Approval Request from Purchase Orders """
        res = super().action_cancel()
        purchase_orders_data_per_state = self._cancel_approval_request()
        self._log_po_cancellation_to_chatter(purchase_orders_data_per_state)
        return res

    def _cancel_approval_request(self):
        purchase_orders = self.sudo().product_line_ids.purchase_order_line_id.order_id
        purchase_orders_data_per_state = {"removed": [], "require_manual_action": []}
        for purchase_order in purchase_orders:
            product_lines = self.sudo().product_line_ids.filtered(
                lambda line: line.purchase_order_line_id.order_id.id == purchase_order.id
            )

            if purchase_order.state == 'draft':
                purchase_orders_data_per_state["removed"].extend(self._get_order_data_from_product_lines(product_lines))
                removed_lines = self.sudo().env['purchase.order.line']
                for product_line in product_lines:
                    purchase_order_line = product_line.purchase_order_line_id
                    if purchase_order_line.product_qty == product_line.quantity:
                        removed_lines |= purchase_order_line
                    else:
                        purchase_order_line.product_qty -= product_line.quantity
                if len(purchase_order.order_line) == len(removed_lines):
                    # Purchase orders must be canceled first before deletion
                    purchase_order.write({'state': 'cancel'})
                    purchase_order.unlink()
                elif removed_lines:
                    removed_lines.unlink()

            else:
                purchase_orders_data_per_state["require_manual_action"].extend(self._get_order_data_from_product_lines(product_lines, include_raw_data=True))

            product_lines.purchase_order_line_id = False

        return purchase_orders_data_per_state

    def action_confirm(self):
        for request in self:
            if request.approval_type == 'purchase' and not request.product_line_ids:
                raise UserError(_("You cannot create an empty purchase request."))
        return super().action_confirm()

    def action_create_purchase_orders(self):
        """ Create and/or modifier Purchase Orders. """
        self.ensure_one()
        if self.purchase_order_count:
            return
        self._create_purchase_orders()
        self._log_po_creation_to_chatter()

    def _create_purchase_orders(self):
        self.product_line_ids._check_products_vendor()
        for line in self.product_line_ids:
            seller = line.seller_id or line.product_id.with_company(line.company_id)._select_seller(
                quantity=line.po_uom_qty,
                uom_id=line.product_id.uom_id,
            )
            vendor = seller.partner_id
            po_domain = line._get_purchase_orders_domain(vendor)
            purchase_orders = self.env['purchase.order'].search(po_domain)

            if purchase_orders:
                # Existing RFQ found: check if we must modify an existing
                # purchase order line or create a new one.
                purchase_line = self.env['purchase.order.line'].search([
                    ('order_id', 'in', purchase_orders.ids),
                    ('product_id', '=', line.product_id.id),
                    ('product_uom_id', '=', line.seller_id.product_uom_id.id or line.product_id.uom_id.id),
                ], limit=1)
                purchase_order = self.env['purchase.order']
                if purchase_line:
                    # Compatible po line found, only update the quantity.
                    line.purchase_order_line_id = purchase_line.id
                    purchase_line.product_qty += line.po_uom_qty
                    purchase_order = purchase_line.order_id
                else:
                    # No purchase order line found, create one.
                    purchase_order = purchase_orders[0]
                    seller_uom_qty = line.product_uom_id._compute_quantity(line.quantity, seller.product_uom_id)
                    po_line_vals = self.env['purchase.order.line']._prepare_purchase_order_line(
                        line.product_id,
                        seller_uom_qty,
                        seller.product_uom_id,
                        line.company_id,
                        vendor,
                        purchase_order,
                    )
                    new_po_line = self.env['purchase.order.line'].create(po_line_vals)
                    line.purchase_order_line_id = new_po_line.id
                    purchase_order.order_line = [(4, new_po_line.id)]

                # Add the request name on the purchase order `origin` field.
                new_origin = set([self.name])
                if purchase_order.origin:
                    missing_origin = new_origin - set(purchase_order.origin.split(', '))
                    if missing_origin:
                        purchase_order.write({'origin': purchase_order.origin + ', ' + ', '.join(missing_origin)})
                else:
                    purchase_order.write({'origin': ', '.join(new_origin)})
            else:
                # No RFQ found: create a new one.
                po_vals = line._get_purchase_order_values(vendor)
                new_purchase_order = self.env['purchase.order'].create(po_vals)
                seller_uom_qty = line.product_uom_id._compute_quantity(line.quantity, seller.product_uom_id)
                po_line_vals = self.env['purchase.order.line']._prepare_purchase_order_line(
                    line.product_id,
                    seller_uom_qty,
                    seller.product_uom_id,
                    line.company_id,
                    vendor,
                    new_purchase_order,
                )
                new_po_line = self.env['purchase.order.line'].create(po_line_vals)
                line.purchase_order_line_id = new_po_line.id
                new_purchase_order.order_line = [(4, new_po_line.id)]

    def action_open_purchase_orders(self):
        """ Return the list of purchase orders the approval request created or
        affected in quantity. """
        self.ensure_one()
        purchase_ids = self.product_line_ids.purchase_order_line_id.order_id.ids
        domain = [('id', 'in', purchase_ids)]
        action = {
            'name': _('Purchase Orders'),
            'view_type': 'list',
            'view_mode': 'list,form',
            'res_model': 'purchase.order',
            'type': 'ir.actions.act_window',
            'context': clean_context(self.env.context),   # avoid 'default_name' context key propagation
            'domain': domain,
        }
        return action

    def _log_po_creation_to_chatter(self):
        purchase_orders_data = self._get_order_data_from_product_lines(self.product_line_ids)
        po_creation_chatter_msg = self._generate_po_log_message("created", purchase_orders_data)
        self._message_log(body=po_creation_chatter_msg)

    def _log_po_cancellation_to_chatter(self, purchase_orders_data_per_state):
        po_cancellation_states = ["removed", "require_manual_action"]
        cancellation_log_msg = ""
        for po_state in po_cancellation_states:
            purchase_orders_data = purchase_orders_data_per_state[po_state]
            if purchase_orders_data:
                cancellation_log_msg += self._generate_po_log_message(po_state, purchase_orders_data)
            if po_state == "require_manual_action":
                self._log_cancellation_exception_to_po_chatter(purchase_orders_data)
        self._message_log(body=cancellation_log_msg)

    def _log_cancellation_exception_to_po_chatter(self, purchase_orders_data):
        for purchase_order_data in purchase_orders_data:
            purchase_order_data["order"]._activity_schedule_with_view(
                'mail.mail_activity_data_warning',
                views_or_xmlid='approvals_purchase.exception_approval_request_canceled',
                user_id=self.env.user.id,
                render_context={
                    'approval_requests': self,
                    'product_lines': purchase_order_data["product_lines"],
                }
            )

    def _get_order_data_from_product_lines(self, product_lines, include_raw_data=False):
        """
        Returns a list of dictionaries, each representing the data of a single order.
        Each dictionary has the following structure:
        {
            "order": The purchase order (optional)
            "product_lines": The product lines of the approval request (optional)
            "order_name": The name of the purchase order
            "products": [(product_name, product_quantity), ...] A list of tuples. Each tuple contains product name and product quantity.
        }
        """
        orders_data = list()
        grouped_product_lines = product_lines.grouped(lambda product_line: product_line.purchase_order_line_id.order_id)
        for order_id, lines in grouped_product_lines.items():
            order_data = dict()
            if include_raw_data:
                order_data["order"] = order_id
                order_data["product_lines"] = lines
            order_data["order_name"] = order_id.name
            order_data["products"] = [(order_line.product_id.name, order_line.quantity) for order_line in lines]
            orders_data.append(order_data)
        return orders_data

    def _generate_po_log_message(self, po_state, purchase_orders_data):
        log_msg_header_by_state = {
            'created': _("The following products have been added to the RFQs:"),
            'removed': _("The following products have been removed from the RFQs:"),
            'require_manual_action': _("The following products couldn't be removed because the RFQs are not in draft state:")
        }

        return Markup("%(log_msg_header)s<br> <br> %(purchase_log)s <hr>") % {
            'log_msg_header': log_msg_header_by_state.get(po_state, ""),
            'purchase_log': Markup().join(
                Markup("RFQ %(po_name)s: <br> <ul>%(products_lines)s</ul>") % {
                    'po_name': purchase_order['order_name'],
                    'products_lines': Markup().join(
                        Markup("<li>%(quantity)s %(name)s</li>") % {
                            'name': product_line[0],
                            'quantity': product_line[1]
                        } for product_line in purchase_order["products"]
                    )
                } for purchase_order in purchase_orders_data
            )
        }
```

## File: models/purchase_order.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from collections import defaultdict
from markupsafe import Markup

from odoo import models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def write(self, vals):
        if 'state' in vals:
            orders_changed_state = self.filtered(lambda purchase_order: purchase_order.state != vals['state'])
            if orders_changed_state:
                related_product_lines = self.sudo().env['approval.product.line'].search(
                    domain=[('purchase_order_line_id.order_id', 'in', orders_changed_state.ids)],
                )
                if related_product_lines:
                    grouped_product_lines = defaultdict(lambda: defaultdict(lambda: self.env['approval.product.line']))
                    for product_line in related_product_lines:
                        grouped_product_lines[product_line.approval_request_id][product_line.purchase_order_line_id.order_id] |= product_line
                    self._log_po_state_change_to_approval_request_chatter(vals['state'], grouped_product_lines)
        return super().write(vals)

    def _log_po_state_change_to_approval_request_chatter(self, new_state, grouped_product_lines):
        for approval_request, product_lines_by_purchase_order in grouped_product_lines.items():
            for purchase_order, product_lines in product_lines_by_purchase_order.items():
                state_change_msg = purchase_order._create_state_change_msg(purchase_order.state, new_state, product_lines)
                approval_request._message_log(body=state_change_msg)

    def _create_state_change_msg(self, old_state, new_state, approval_request_products):
        state_label = dict(self._fields['state']._description_selection(self.env))
        return Markup("%(state_change_header)s<br> %(products_summary)s") % {
            'state_change_header': _("RFQ %(rfq_name)s state has been changed: %(old_state_label)s -> %(new_state_label)s",
                rfq_name=self.name,
                old_state_label=state_label[old_state],
                new_state_label=state_label[new_state]),
            'products_summary': Markup("%(header)s<br> <ul>%(products)s</ul>") % {
                'header': _("Products: "),
                'products': Markup().join(
                    Markup("<li>%(product_quantity)s %(product_name)s</li>") % {
                        'product_quantity': product.quantity,
                        'product_name': product.product_id.name
                    } for product in approval_request_products
                )
            }
        }
```

## File: models/res_partner.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _default_category(self):
        if self.env.context.get('unset_res_partner_category_id'):
            return False
        return super()._default_category()

    category_id = fields.Many2many(default=_default_category)
```

## File: views/approval_category_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="approval_purchase_category_view_form_inherit" model="ir.ui.view">
        <field name="name">approval.purchase.category.view.form.inherit</field>
        <field name="model">approval.category</field>
        <field name="inherit_id" ref="approvals.approval_category_view_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='approval_type']" position="attributes">
                <attribute name="invisible">0</attribute>
            </xpath>
            <xpath expr="//field[@name='has_quantity']" position="attributes">
                <attribute name="readonly">approval_type == 'purchase'</attribute>
                <attribute name="force_save">1</attribute>
            </xpath>
            <xpath expr="//field[@name='has_product']" position="attributes">
                <attribute name="readonly">approval_type == 'purchase'</attribute>
                <attribute name="force_save">1</attribute>
            </xpath>
        </field>
    </record>
</odoo>
```

## File: views/approval_product_line_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="approval_purchase_product_line_view_tree_inherit" model="ir.ui.view">
        <field name="name">approval.purchase.product.line.view.list.inherit</field>
        <field name="model">approval.product.line</field>
        <field name="inherit_id" ref="approvals.approval_product_line_view_tree"/>
        <field name="arch" type="xml">
            <xpath expr="//list" position="attributes">
                <attribute name="decoration-danger">has_no_seller</attribute>
            </xpath>
            <xpath expr="//field[@name='product_id']" position="attributes">
                <attribute name="required">parent.approval_type != 'purchase' and parent.has_product == 'required'</attribute>
            </xpath>
            <xpath expr="//field[@name='product_uom_id']" position="after">
                <field name="seller_id" column_invisible="parent.approval_type != 'purchase'"
                    domain="[('product_tmpl_id', '=', product_template_id)]"
                    options="{'no_quick_create': True}"
                    context="{
                        'default_product_tmpl_id': product_template_id,
                        'default_product_id': product_id,
                        'unset_res_partner_category_id': True,
                    }"/>
            </xpath>
        </field>
    </record>
</odoo>
```

## File: views/approval_request_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="approval_purchase_request_view_form_inherit" model="ir.ui.view">
        <field name="name">approval.purchase.request.view.form.inherit</field>
        <field name="model">approval.request</field>
        <field name="inherit_id" ref="approvals.approval_request_view_form"/>
        <field name="arch" type="xml">
            <xpath expr="//button[@name='action_get_attachment_view']" position="after">
                <button name="action_open_purchase_orders" type="object"
                    groups="purchase.group_purchase_user"
                    class="oe_stat_button" icon="fa-credit-card"
                    invisible="purchase_order_count == 0">
                    <field name="purchase_order_count" string="Purchase Orders"
                        groups="purchase.group_purchase_user" widget="statinfo"/>
                </button>
            </xpath>
            <xpath expr="//button[@name='action_confirm']" position="after">
                <button name="action_create_purchase_orders" type="object"
                    groups="purchase.group_purchase_user"
                    string="Create RFQ's" class="btn-primary"
                    data-hotkey="g" invisible="approval_type != 'purchase' or request_status != 'approved' or purchase_order_count &gt; 0"/>
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
    'name': 'Approvals - Purchase',
    'version': '1.0',
    'category': 'Human Resources/Approvals',
    'description': """
This module adds to the approvals workflow the possibility to generate
RFQ from an approval purchase request.
    """,
    'depends': ['approvals', 'purchase'],
    'data': [
        'data/approval_category_data.xml',
        'data/mail_templates.xml',
        'views/approval_category_views.xml',
        'views/approval_product_line_views.xml',
        'views/approval_request_views.xml',
    ],
    'demo': [
        'data/approval_demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'author': 'Odoo S.A.',
    'license': 'OEEL-1',
}
```
