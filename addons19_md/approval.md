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
  mail_activity_type_data.xml
  mail_message_subtype_data.xml
models/
  __init__.py
  approval_approver.py
  approval_category_approver.py
  approval_category.py
  approval_product_line.py
  approval_request.py
  ir_attachment.py
  mail_activity_type.py
  mail_activity.py
report/
  approval_request_report.xml
security/
  approval_security.xml
  ir.model.access.csv
static/
  description/
    icon_hi.png
    icon.png
    icon.svg
  src/
    common/
      activity_model_patch.js
      approver_model.js
    img/
      Award.png
      Bag.png
      Books.png
      Car.png
      Contract.png
      Credit-card.png
      Folder.png
      Suitcase.png
    scss/
      approvals.scss
    views/
      kanban/
        approvals_category_kanban_controller.js
        approvals_category_kanban_controller.xml
        approvals_category_kanban_view.js
    web/
      activity_list_popover_item_patch.js
      activity_list_popover_item_patch.xml
      activity_patch.js
      activity_patch.xml
      approval.js
      approval.xml
  tests/
    mock_server/
      mock_models/
        approval_approver.js
        approval_request.js
        mail_activity.js
    tours/
      approvals.js
    activity_patch.test.js
    approvals_test_helpers.js
views/
  approval_category_approver_views.xml
  approval_category_views.xml
  approval_product_line_views.xml
  approval_products_views.xml
  approval_request_template.xml
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
        <record id="base.user_admin" model="res.users">
            <field eval="[(4, ref('approvals.group_approval_manager'))]" name="group_ids"/>
        </record>

        <record id="approval_category_data_business_trip" model="approval.category">
            <field name="name">Business Trip</field>
            <field name="image" type="base64" file="approvals/static/src/img/Suitcase.png"/>
            <field name="sequence">1</field>
            <field name="has_date">no</field>
            <field name="has_period">required</field>
            <field name="has_product">no</field>
            <field name="has_quantity">no</field>
            <field name="has_amount">no</field>
            <field name="has_reference">no</field>
            <field name="has_partner">no</field>
            <field name="has_payment_method">no</field>
            <field name="has_location">required</field>
            <field name="requirer_document">optional</field>
            <field name="approval_minimum">1</field>
            <field name="manager_approval">approver</field>
        </record>
        <record id="approval_category_data_borrow_items" model="approval.category">
            <field name="name">Borrow Items</field>
            <field name="image" type="base64" file="approvals/static/src/img/Books.png"/>
            <field name="sequence">10</field>
            <field name="has_date">no</field>
            <field name="has_period">required</field>
            <field name="has_product">required</field>
            <field name="has_quantity">optional</field>
            <field name="has_amount">no</field>
            <field name="has_reference">no</field>
            <field name="has_partner">no</field>
            <field name="has_payment_method">no</field>
            <field name="has_location">no</field>
            <field name="requirer_document">optional</field>
            <field name="approval_minimum">1</field>
        </record>
        <record id="approval_category_data_general_approval" model="approval.category">
            <field name="name">General Approval</field>
            <field name="image" type="base64" file="approvals/static/src/img/Folder.png"/>
            <field name="sequence">20</field>
            <field name="has_date">optional</field>
            <field name="has_period">optional</field>
            <field name="has_product">optional</field>
            <field name="has_quantity">optional</field>
            <field name="has_amount">optional</field>
            <field name="has_reference">optional</field>
            <field name="has_partner">optional</field>
            <field name="has_payment_method">optional</field>
            <field name="has_location">optional</field>
            <field name="requirer_document">required</field>
            <field name="approval_minimum">1</field>
            <field name="manager_approval">approver</field>
        </record>
        <record id="approval_category_data_contract_approval" model="approval.category">
            <field name="name">Contract Approval</field>
            <field name="image" type="base64" file="approvals/static/src/img/Contract.png"/>
            <field name="sequence">30</field>
            <field name="has_date">no</field>
            <field name="has_period">no</field>
            <field name="has_product">no</field>
            <field name="has_quantity">no</field>
            <field name="has_amount">optional</field>
            <field name="has_reference">required</field>
            <field name="has_partner">required</field>
            <field name="has_payment_method">no</field>
            <field name="has_location">no</field>
            <field name="requirer_document">optional</field>
            <field name="approval_minimum">1</field>
        </record>
        <record id="approval_category_data_payment_application" model="approval.category">
            <field name="name">Payment Application</field>
            <field name="image" type="base64" file="approvals/static/src/img/Credit-card.png"/>
            <field name="sequence">40</field>
            <field name="has_date">required</field>
            <field name="has_period">no</field>
            <field name="has_product">no</field>
            <field name="has_quantity">no</field>
            <field name="has_amount">required</field>
            <field name="has_reference">no</field>
            <field name="has_partner">required</field>
            <field name="has_payment_method">required</field>
            <field name="has_location">no</field>
            <field name="requirer_document">optional</field>
            <field name="approval_minimum">1</field>
        </record>
        <record id="approval_category_data_car_rental_application" model="approval.category">
            <field name="name">Car Rental Application</field>
            <field name="image" type="base64" file="approvals/static/src/img/Car.png"/>
            <field name="sequence">50</field>
            <field name="has_date">no</field>
            <field name="has_period">required</field>
            <field name="has_product">no</field>
            <field name="has_quantity">no</field>
            <field name="has_amount">no</field>
            <field name="has_reference">no</field>
            <field name="has_partner">no</field>
            <field name="has_payment_method">no</field>
            <field name="has_location">no</field>
            <field name="requirer_document">optional</field>
            <field name="approval_minimum">1</field>
        </record>
        <record id="approval_category_data_job_referral_award" model="approval.category">
            <field name="name">Job Referral Award</field>
            <field name="image" type="base64" file="approvals/static/src/img/Award.png"/>
            <field name="sequence">60</field>
            <field name="has_date">no</field>
            <field name="has_period">no</field>
            <field name="has_product">no</field>
            <field name="has_quantity">no</field>
            <field name="has_amount">no</field>
            <field name="has_reference">no</field>
            <field name="has_partner">required</field>
            <field name="has_payment_method">no</field>
            <field name="has_location">no</field>
            <field name="requirer_document">optional</field>
            <field name="approval_minimum">1</field>
        </record>
        <record id="approval_category_data_procurement" model="approval.category">
            <field name="name">Procurement</field>
            <field name="image" type="base64" file="approvals/static/src/img/Bag.png"/>
            <field name="sequence">70</field>
            <field name="has_date">no</field>
            <field name="has_period">no</field>
            <field name="has_product">no</field>
            <field name="has_quantity">required</field>
            <field name="has_amount">optional</field>
            <field name="has_reference">no</field>
            <field name="has_partner">no</field>
            <field name="has_payment_method">no</field>
            <field name="has_location">no</field>
            <field name="requirer_document">optional</field>
            <field name="approval_minimum">1</field>
        </record>
    </data>
</odoo>
```

## File: data/approval_demo.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <record id="base.user_demo" model="res.users">
            <field name="group_ids" eval="[
                (3, ref('approvals.group_approval_user')),
                (3, ref('approvals.group_approval_manager')),
            ]"/>
        </record>

        <record id="base.default_user_group" model="res.groups">
            <field name="implied_ids" eval="[(4, ref('approvals.group_approval_manager'))]"/>
        </record>

        <record id="approval_request_demo_business_trip" model="approval.request">
            <field name="name">Business trip to London</field>
            <field name="request_status">pending</field>
            <field name="location">London</field>
            <field name="category_id" ref="approval_category_data_business_trip"/>
            <field name="request_owner_id" ref="base.user_admin"/>
            <field name="date_start" eval="time.strftime('%Y-05-01')"/>
            <field name="date_end" eval="time.strftime('%Y-05-05')"/>
            <field name="reason">Meeting with a potential customer.</field>
        </record>

        <record id="approval_approver_business_trip_1" model="approval.approver">
            <field name="user_id" ref="base.user_demo"/>
            <field name="request_id" ref="approval_request_demo_business_trip"/>
        </record>

        <record id="approval_request_demo_borrow_items" model="approval.request">
            <field name="name">Borrow the screwdriver</field>
            <field name="request_status">pending</field>
            <field name="category_id" ref="approval_category_data_borrow_items"/>
            <field name="request_owner_id" ref="base.user_demo"/>
            <field name="date_start" eval="time.strftime('%Y-05-01')"/>
            <field name="date_end" eval="time.strftime('%Y-05-01')"/>
            <field name="product_line_ids" eval="[(0, 0, {'description': 'Screwdriver X15'})]"/>
            <field name="reason">Need a screwdriver to fix the main door.</field>
        </record>

        <record id="approval_approver_borrow_items_1" model="approval.approver">
            <field name="user_id" ref="base.user_admin"/>
            <field name="request_id" ref="approval_request_demo_borrow_items"/>
        </record>

        <record id="approval_approver_borrow_items_2" model="approval.approver">
            <field name="user_id" ref="base.user_demo"/>
            <field name="request_id" ref="approval_request_demo_borrow_items"/>
        </record>

        <record id="approval_category_data_business_trip" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>

        <record id="approval_category_data_borrow_items" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>

        <record id="approval_category_data_general_approval" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>

        <record id="approval_category_data_contract_approval" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>

        <record id="approval_category_data_payment_application" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>

        <record id="approval_category_data_car_rental_application" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>

        <record id="approval_category_data_job_referral_award" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>

        <record id="approval_category_data_procurement" model="approval.category">
            <field name="approver_ids" eval="[(0, 0, {'user_id': ref('base.user_admin')})]"/>
        </record>
    </data>
</odoo>
```

## File: data/mail_activity_type_data.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data noupdate="1">
        <record id="mail_activity_data_approval" model="mail.activity.type">
            <field name="name">Approval</field>
            <field name="icon">fa-check-circle</field>
            <field name="sequence">4</field>
            <field name="active">False</field>
            <field name="res_model">approval.request</field>
        </record>
    </data>
</odoo>
```

## File: data/mail_message_subtype_data.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo noupdate="1">
    <record id="mt_approval_request_status" model="mail.message.subtype">
        <field name="name">Approval Status Change</field>
        <field name="res_model">Approval.Request</field>
        <field name="default" eval="False"/>
        <field name="description">Approval Status Change</field>
        <field name="sequence">5</field>
    </record>
</odoo>
```

## File: models/__init__.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import approval_approver
from . import approval_category
from . import approval_category_approver
from . import approval_product_line
from . import approval_request
from . import mail_activity
from . import mail_activity_type
from . import ir_attachment
```

## File: models/approval_approver.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, models, fields, api
from odoo.exceptions import AccessError


class ApprovalApprover(models.Model):
    _name = 'approval.approver'
    _description = 'Approver'
    _order = 'sequence, id'

    _check_company_auto = True

    sequence = fields.Integer('Sequence', default=10)
    user_id = fields.Many2one('res.users', string="User", required=True, check_company=True,
        domain="""
            [
                ('share', '=', False),
                '|',
                    ('id', 'not in', existing_request_user_ids),
                    ('id', '=', user_id)
            ]
        """)
    existing_request_user_ids = fields.Many2many('res.users', compute='_compute_existing_request_user_ids')
    status = fields.Selection([
        ('new', 'New'),
        ('pending', 'To Approve'),
        ('waiting', 'Waiting'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('cancel', 'Cancel')], string="Status", default="new", readonly=True)
    request_id = fields.Many2one('approval.request', string="Request",
        index='btree_not_null', ondelete='cascade', check_company=True)
    company_id = fields.Many2one(
        string='Company', related='request_id.company_id',
        store=True, readonly=True, index=True)
    required = fields.Boolean(default=False, readonly=True)
    category_approver = fields.Boolean(compute='_compute_category_approver')
    can_edit = fields.Boolean(compute='_compute_can_edit')
    can_edit_user_id = fields.Boolean(compute='_compute_can_edit', help="Simple users should not be able to remove themselves as approvers because they will lose access to the record if they misclick.")

    def write(self, vals):
        if 'request_id' in vals:
            request = self.env['approval.request'].browse(vals['request_id'])
            request.check_access('write')
            if self.request_id and self.request_id != request:
                raise AccessError(_("You cannot change approval request."))
        return super().write(vals)

    def action_approve(self):
        self.request_id.action_approve(self)

    def action_refuse(self):
        self.request_id.action_refuse(self)

    def _create_activity(self):
        for approver in self:
            approver.request_id.activity_schedule(
                'approvals.mail_activity_data_approval',
                user_id=approver.user_id.id)

    @api.depends('request_id.request_owner_id', 'request_id.approver_ids.user_id')
    def _compute_existing_request_user_ids(self):
        for approver in self:
            approver.existing_request_user_ids = \
                self.mapped('request_id.approver_ids.user_id')._origin \
              | self.request_id.request_owner_id._origin

    @api.depends('category_approver', 'user_id')
    def _compute_category_approver(self):
        for approval in self:
            approval.category_approver = approval.user_id in approval.request_id.category_id.approver_ids.user_id

    @api.depends_context('uid')
    @api.depends('user_id', 'category_approver')
    def _compute_can_edit(self):
        is_user = self.env.user.has_group('approvals.group_approval_user')
        for approval in self:
            approval.can_edit = is_user
            approval.can_edit_user_id = is_user or not approval.user_id

    _unique_request_user = models.Constraint(
        'UNIQUE(request_id, user_id)',
        "An approver with the same user already exists for this request.",
    )
```

## File: models/approval_category_approver.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ApprovalCategoryApprover(models.Model):
    """ Intermediate model between approval.category and res.users
        To know whether an approver for this category is required or not
    """
    _name = 'approval.category.approver'
    _description = 'Approval Category Approver'
    _rec_name = 'user_id'
    _order = 'sequence'

    sequence = fields.Integer('Sequence', default=10)
    category_id = fields.Many2one('approval.category', string='Approval Category', ondelete='cascade', required=True, index=True)
    company_id = fields.Many2one('res.company', related='category_id.company_id')
    user_id = fields.Many2one('res.users', string='User', ondelete='cascade', required=True,
        check_company=True, domain="[('company_ids', 'in', company_id), ('id', 'not in', existing_user_ids)]")
    required = fields.Boolean(default=False)

    existing_user_ids = fields.Many2many('res.users', compute='_compute_existing_user_ids')

    @api.depends('category_id')
    def _compute_existing_user_ids(self):
        for record in self:
            record.existing_user_ids = record.category_id.approver_ids.user_id
```

## File: models/approval_category.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


CATEGORY_SELECTION = [
    ('required', 'Required'),
    ('optional', 'Optional'),
    ('no', 'None')]


class ApprovalCategory(models.Model):
    _name = 'approval.category'
    _description = 'Approval Category'
    _order = 'sequence, id'

    _check_company_auto = True

    def _get_default_image(self):
        with tools.file_open('approvals/static/src/img/Folder.png', 'rb') as f:
            return base64.b64encode(f.read())

    name = fields.Char(string="Name", translate=True, required=True)
    company_id = fields.Many2one(
        'res.company', 'Company', copy=False,
        required=True, index=True, default=lambda s: s.env.company)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(string="Sequence")
    description = fields.Char(string="Description", translate=True)
    image = fields.Binary(string='Image', default=_get_default_image)
    has_date = fields.Selection(CATEGORY_SELECTION, string="Has Date", default="no", required=True)
    has_period = fields.Selection(CATEGORY_SELECTION, string="Has Period", default="no", required=True)
    has_quantity = fields.Selection(CATEGORY_SELECTION, string="Has Quantity", default="no", required=True)
    has_amount = fields.Selection(CATEGORY_SELECTION, string="Has Amount", default="no", required=True)
    has_reference = fields.Selection(
        CATEGORY_SELECTION, string="Has Reference", default="no", required=True,
        help="An additional reference that should be specified on the request.")
    has_partner = fields.Selection(CATEGORY_SELECTION, string="Has Contact", default="no", required=True)
    has_payment_method = fields.Selection(CATEGORY_SELECTION, string="Has Payment", default="no", required=True)
    has_location = fields.Selection(CATEGORY_SELECTION, string="Has Location", default="no", required=True)
    has_product = fields.Selection(
        CATEGORY_SELECTION, string="Has Product", default="no", required=True,
        help="Additional products that should be specified on the request.")
    requirer_document = fields.Selection([('required', 'Required'), ('optional', 'Optional')], string="Documents", default="optional", required=True)
    approval_minimum = fields.Integer(string="Minimum Approval", default="1", required=True)
    invalid_minimum = fields.Boolean(compute='_compute_invalid_minimum')
    invalid_minimum_warning = fields.Char(compute='_compute_invalid_minimum')
    approval_type = fields.Selection(string="Approval Type", selection=[],
        help="Allows you to define which documents you would like to create once the request has been approved")
    manager_approval = fields.Selection([('approver', 'Is Approver'), ('required', 'Is Required Approver')],
        string="Employee's Manager",
        help="""How the employee's manager interacts with this type of approval.

        Empty: do nothing
        Is Approver: the employee's manager will be in the approver list
        Is Required Approver: the employee's manager will be required to approve the request.
    """)
    user_ids = fields.Many2many('res.users', compute='_compute_user_ids', string="Approver Users")
    approver_ids = fields.One2many('approval.category.approver', 'category_id', string="Approvers")
    approver_sequence = fields.Boolean('Approvers Sequence?', help="If checked, the approvers have to approve in sequence (one after the other). If Employee's Manager is selected as approver, they will be the first in line.")
    request_to_validate_count = fields.Integer("Number of requests to validate", compute="_compute_request_to_validate_count")
    automated_sequence = fields.Boolean('Automated Sequence?',
        help="If checked, the Approval Requests will have an automated generated name based on the given code.")
    sequence_code = fields.Char(string="Code")
    sequence_id = fields.Many2one('ir.sequence', 'Reference Sequence',
        copy=False, check_company=True)
    approval_properties_definition = fields.PropertiesDefinition('Approval Properties')

    def _compute_request_to_validate_count(self):
        domain = [('request_status', '=', 'pending'), ('approver_ids.user_id', '=', self.env.user.id)]
        requests_data = self.env['approval.request']._read_group(domain, ['category_id'], ['__count'])
        requests_mapped_data = {category.id: count for category, count in requests_data}
        for category in self:
            category.request_to_validate_count = requests_mapped_data.get(category.id, 0)

    @api.depends_context('lang')
    @api.depends('approval_minimum', 'approver_ids', 'manager_approval')
    def _compute_invalid_minimum(self):
        for record in self:
            if record.approval_minimum > len(record.approver_ids) + int(bool(record.manager_approval)):
                record.invalid_minimum = True
            else:
                record.invalid_minimum = False
            record.invalid_minimum_warning = record.invalid_minimum and _('Your minimum approval exceeds the total of default approvers.')

    @api.depends('approver_ids')
    def _compute_user_ids(self):
        for record in self:
            record.user_ids = record.approver_ids.user_id

    @api.constrains('approval_minimum', 'approver_ids')
    def _constrains_approval_minimum(self):
        for record in self:
            if record.approval_minimum < len(record.approver_ids.filtered('required')):
                raise ValidationError(_('Minimum Approval must be equal or superior to the sum of required Approvers.'))

    @api.constrains('approver_ids')
    def _constrains_approver_ids(self):
        # There seems to be a problem with how the database is updated which doesn't let use to an sql constraint for this
        # Issue is: records seem to be created before others are saved, meaning that if you originally have only user a
        #  change user a to user b and add a new line with user a, the second line will be created and will trigger the constraint
        #  before the first line will be updated which wouldn't trigger a ValidationError
        for record in self:
            if len(record.approver_ids) != len(record.approver_ids.user_id):
                raise ValidationError(_('An user may not be in the approver list multiple times.'))

    @api.constrains('approver_sequence', 'approval_minimum')
    def _constrains_approver_sequence(self):
        if any(a.approver_sequence and not a.approval_minimum for a in self):
            raise ValidationError(_('Approver Sequence can only be activated with at least 1 minimum approver.'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('automated_sequence'):
                sequence = self.env['ir.sequence'].create({
                    'name': _('Sequence %(code)s', code=vals['sequence_code']),
                    'padding': 5,
                    'prefix': vals['sequence_code'],
                    'company_id': vals.get('company_id'),
                })
                vals['sequence_id'] = sequence.id
        return super().create(vals_list)

    def write(self, vals):
        if 'sequence_code' in vals:
            for approval_category in self:
                sequence_vals = {
                    'name': _('Sequence %(code)s', code=vals['sequence_code']),
                    'padding': 5,
                    'prefix': vals['sequence_code'],
                }
                if approval_category.sequence_id:
                    approval_category.sequence_id.write(sequence_vals)
                else:
                    sequence_vals['company_id'] = vals.get('company_id', approval_category.company_id.id)
                    sequence = self.env['ir.sequence'].create(sequence_vals)
                    approval_category.sequence_id = sequence
        if 'company_id' in vals:
            for approval_category in self:
                if approval_category.sequence_id:
                    approval_category.sequence_id.company_id = vals.get('company_id')
        return super().write(vals)

    def create_request(self):
        self.ensure_one()
        # If category uses sequence, set next sequence as name
        # (if not, set category name as default name).
        return {
            "type": "ir.actions.act_window",
            "res_model": "approval.request",
            "views": [[False, "form"]],
            "context": {
                'default_name': _('New') if self.automated_sequence else self.name,
                'default_category_id': self.id,
                'default_request_owner_id': self.env.user.id,
                'default_request_status': 'new'
            },
        }
```

## File: models/approval_product_line.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ApprovalProductLine(models.Model):
    _name = 'approval.product.line'
    _description = 'Product Line'

    _check_company_auto = True

    approval_request_id = fields.Many2one('approval.request', required=True, index=True)
    description = fields.Char(
        "Description", required=True,
        compute="_compute_description", store=True, readonly=False, precompute=True)
    company_id = fields.Many2one(
        string='Company', related='approval_request_id.company_id',
        store=True, readonly=True, index=True)
    product_id = fields.Many2one('product.product', string="Products", check_company=True)
    product_uom_id = fields.Many2one(
        'uom.uom', string="Unit",
        compute="_compute_product_uom_id", store=True, readonly=False, precompute=True)
    quantity = fields.Float("Quantity", default=1.0)

    @api.depends('product_id')
    def _compute_description(self):
        for line in self:
            line.description = line.product_id.description_purchase or line.product_id.display_name

    @api.depends('product_id')
    def _compute_product_uom_id(self):
        for line in self:
            line.product_uom_id = line.product_id.uom_id
```

## File: models/approval_request.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, Command, fields, models, _
from odoo.exceptions import AccessError, UserError, ValidationError


class ApprovalRequest(models.Model):
    _name = 'approval.request'
    _description = 'Approval Request'
    _inherit = ['mail.thread.main.attachment', 'mail.activity.mixin']
    _order = 'name'
    _mail_post_access = 'read'

    _check_company_auto = True

    def _get_request_owner_id_domain(self):
        return [('share', '=', False), ('company_ids', 'in', self.env.companies.ids)]

    name = fields.Char(string="Approval Subject", tracking=True)
    active = fields.Boolean(default=True, tracking=True)
    category_id = fields.Many2one('approval.category', string="Category", required=True)
    category_image = fields.Binary(related='category_id.image')
    approver_ids = fields.One2many('approval.approver', 'request_id', string="Approvers", check_company=True,
        compute='_compute_approver_ids', store=True, readonly=False)
    user_ids = fields.Many2many('res.users', string="Users",
        compute='_compute_user_ids', readonly=True)
    company_id = fields.Many2one(
        string='Company', related='category_id.company_id',
        store=True, readonly=True, index=True)
    date = fields.Datetime(string="Date")
    date_start = fields.Datetime(string="Date start")
    date_end = fields.Datetime(string="Date end")
    quantity = fields.Float(string="Quantity")
    location = fields.Char(string="Location")
    date_confirmed = fields.Datetime(string="Date Confirmed")
    partner_id = fields.Many2one('res.partner', string="Contact", check_company=True)
    reference = fields.Char(string="Reference")
    amount = fields.Float(string="Amount")
    reason = fields.Html(string="Description")
    request_status = fields.Selection([
        ('new', 'To Submit'),
        ('pending', 'Submitted'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('cancel', 'Canceled'),
    ], default="new", compute="_compute_request_status",
        store=True, index=True, tracking=True,
        group_expand=True)
    request_owner_id = fields.Many2one('res.users', string="Request Owner",
        check_company=True, domain=_get_request_owner_id_domain,
        default=lambda self: self.env.user)
    user_status = fields.Selection([
        ('new', 'New'),
        ('pending', 'Submitted'),
        ('waiting', 'Waiting'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('cancel', 'Canceled')], compute="_compute_user_status")
    has_access_to_request = fields.Boolean(string="Has Access To Request", compute="_compute_has_access_to_request")
    change_request_owner = fields.Boolean(string='Can Change Request Owner', compute='_compute_has_access_to_request')
    attachment_ids = fields.One2many(comodel_name='ir.attachment', inverse_name='res_id', domain=[('res_model', '=', 'approval.request')], string='Attachments')
    attachment_number = fields.Integer('Number of Attachments', compute='_compute_attachment_number')
    product_line_ids = fields.One2many('approval.product.line', 'approval_request_id', check_company=True)
    approval_properties = fields.Properties('Properties', definition='category_id.approval_properties_definition')

    has_date = fields.Selection(related="category_id.has_date")
    has_period = fields.Selection(related="category_id.has_period")
    has_quantity = fields.Selection(related="category_id.has_quantity")
    has_amount = fields.Selection(related="category_id.has_amount")
    has_reference = fields.Selection(related="category_id.has_reference")
    has_partner = fields.Selection(related="category_id.has_partner")
    has_payment_method = fields.Selection(related="category_id.has_payment_method")
    has_location = fields.Selection(related="category_id.has_location")
    has_product = fields.Selection(related="category_id.has_product")
    requirer_document = fields.Selection(related="category_id.requirer_document")
    approval_minimum = fields.Integer(related="category_id.approval_minimum")
    approval_type = fields.Selection(related="category_id.approval_type")
    approver_sequence = fields.Boolean(related="category_id.approver_sequence")
    automated_sequence = fields.Boolean(related="category_id.automated_sequence")

    @api.depends('approver_ids')
    def _compute_user_ids(self):
        for request in self:
            request.user_ids = request.approver_ids.user_id

    @api.depends('request_owner_id')
    @api.depends_context('uid')
    def _compute_has_access_to_request(self):
        is_approval_user = self.env.user.has_group('approvals.group_approval_user')
        self.change_request_owner = is_approval_user
        for request in self:
            request.has_access_to_request = request.request_owner_id == self.env.user and is_approval_user

    def _compute_attachment_number(self):
        domain = [('res_model', '=', 'approval.request'), ('res_id', 'in', self.ids)]
        attachment_data = self.env['ir.attachment']._read_group(domain, ['res_id'], ['__count'])
        attachment = dict(attachment_data)
        for request in self:
            request.attachment_number = attachment.get(request.id, 0)

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for request in self:
            if request.date_start and request.date_end and request.date_start > request.date_end:
                raise ValidationError(_("Start date should precede the end date."))

    def copy_data(self, default=None):
        vals_list = super().copy_data(default=default)
        return [dict(vals, name=self.env._("%s (copy)", request.name)) for request, vals in zip(self, vals_list)]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            category = 'category_id' in vals and self.env['approval.category'].browse(vals['category_id'])
            if category and category.automated_sequence:
                vals['name'] = category.sequence_id.next_by_id()
        created_requests = super().create(vals_list)
        for request in created_requests:
            request.message_subscribe(partner_ids=request.request_owner_id.partner_id.ids)
        return created_requests

    @api.ondelete(at_uninstall=False)
    def unlink_attachments(self):
        attachment_ids = self.env['ir.attachment'].search([
            ('res_model', '=', 'approval.request'),
            ('res_id', 'in', self.ids),
        ])
        if attachment_ids:
            attachment_ids.unlink()

    @api.ondelete(at_uninstall=False)
    def _unlink_except_status_is_approved(self):
        for request in self:
            if request.request_status == 'approved':
                raise UserError(_("You can't delete an approved request. Archive it instead."))

    def unlink(self):
        self.filtered(lambda a: a.has_product).product_line_ids.unlink()
        return super().unlink()

    def action_get_attachment_view(self):
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id('base.action_attachment')
        res['domain'] = [('res_model', '=', 'approval.request'), ('res_id', 'in', self.ids)]
        res['context'] = {'default_res_model': 'approval.request', 'default_res_id': self.id}
        return res

    def action_confirm(self):
        # make sure that the manager is present in the list if he is required
        self.ensure_one()
        if self.category_id.manager_approval == 'required':
            employee = self.env['hr.employee'].search([('user_id', '=', self.request_owner_id.id), ('company_id', '=', self.company_id.id)], limit=1)
            if not employee.parent_id:
                raise UserError(_('This request needs to be approved by your manager. There is no manager linked to your employee profile.'))
            if not employee.parent_id.user_id:
                raise UserError(_('This request needs to be approved by your manager. There is no user linked to your manager.'))
            if not self.approver_ids.filtered(lambda a: a.user_id.id == employee.parent_id.user_id.id):
                raise UserError(_('This request needs to be approved by your manager. Your manager is not in the approvers list.'))
        if len(self.approver_ids) < self.approval_minimum:
            raise UserError(_("You have to add at least %s approvers to confirm your request.", self.approval_minimum))
        if self.requirer_document == 'required' and not self.attachment_number:
            raise UserError(_("You have to attach at least one document."))

        approvers = self.approver_ids
        if self.approver_sequence:
            approvers = approvers.filtered(lambda a: a.status in ['new', 'pending', 'waiting'])

            approvers[1:].sudo().write({'status': 'waiting'})
            approvers = approvers[0] if approvers and approvers[0].status != 'pending' else self.env['approval.approver']
        else:
            approvers = approvers.filtered(lambda a: a.status == 'new')

        approvers._create_activity()
        approvers.sudo().write({'status': 'pending'})
        self.sudo().write({'date_confirmed': fields.Datetime.now()})

    def _get_user_approval_activities(self, user):
        domain = [
            ('res_model', '=', 'approval.request'),
            ('res_id', 'in', self.ids),
            ('activity_type_id', '=', self.env.ref('approvals.mail_activity_data_approval').id),
            ('user_id', '=', user.id)
        ]
        activities = self.env['mail.activity'].search(domain)
        return activities

    def _update_next_approvers(self, new_status, approver, only_next_approver, cancel_activities=False):
        approvers_updated = self.env['approval.approver']
        for approval in self.filtered('approver_sequence'):
            current_approver = approval.approver_ids & approver
            approvers_to_update = approval.approver_ids.filtered(lambda a: a.status not in ['approved', 'refused'] and (a.sequence > current_approver.sequence or (a.sequence == current_approver.sequence and a.id > current_approver.id)))

            if only_next_approver and approvers_to_update:
                approvers_to_update = approvers_to_update[0]
            approvers_updated |= approvers_to_update

        approvers_updated.sudo().status = new_status
        if new_status == 'pending':
            approvers_updated._create_activity()
        if cancel_activities:
            approvers_updated.request_id._cancel_activities()

    def _cancel_activities(self):
        approval_activity = self.env.ref('approvals.mail_activity_data_approval')
        activities = self.activity_ids.filtered(lambda a: a.activity_type_id == approval_activity)
        activities.unlink()

    def _action_force_approval(self):
        if not self.env.user.has_group('approvals.group_approval_user'):
            raise UserError(_('You do not have the rights to execute that action.'))
        approval_requests = self.filtered(lambda request: request.request_status in ('pending', 'refused'))
        approval_requests.approver_ids.write({'status': 'approved'})
        approval_requests._cancel_activities()
        for approval_request in approval_requests:
            approval_request.message_post(body=_('The request has been approved by an Approval Officer'))

    def action_approve(self, approver=None):
        if any(approval.approver_sequence and approval.user_status == 'waiting' for approval in self):
            raise ValidationError(_('You cannot approve before the previous approver.'))

        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'approved'})
        self.sudo()._update_next_approvers('pending', approver, only_next_approver=True)
        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()

    def action_refuse(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        approver.write({'status': 'refused'})
        self.sudo()._update_next_approvers('refused', approver, only_next_approver=False, cancel_activities=True)
        self.sudo()._get_user_approval_activities(user=self.env.user).action_feedback()

    def action_withdraw(self, approver=None):
        if not isinstance(approver, models.BaseModel):
            approver = self.mapped('approver_ids').filtered(
                lambda approver: approver.user_id == self.env.user
            )
        self.sudo()._update_next_approvers('waiting', approver, only_next_approver=False, cancel_activities=True)
        approver.write({'status': 'pending'})

    def action_draft(self):
        self.mapped('approver_ids').write({'status': 'new'})

    def action_cancel(self):
        self.sudo()._get_user_approval_activities(user=self.env.user).unlink()
        self.mapped('approver_ids').write({'status': 'cancel'})

    @api.depends_context('uid')
    @api.depends('approver_ids.status')
    def _compute_user_status(self):
        for approval in self:
            approval.user_status = approval.approver_ids.filtered(lambda approver: approver.user_id == self.env.user).status

    @api.depends('approver_ids.status', 'approver_ids.required')
    def _compute_request_status(self):
        for request in self:
            old_status = request.request_status
            status_lst = request.mapped('approver_ids.status')
            required_approved = all(a.status == 'approved' for a in request.approver_ids.filtered('required'))
            minimal_approver = request.approval_minimum if len(status_lst) >= request.approval_minimum else len(status_lst)
            if status_lst:
                if status_lst.count('cancel'):
                    status = 'cancel'
                elif status_lst.count('refused'):
                    status = 'refused'
                elif status_lst.count('new'):
                    status = 'new'
                elif status_lst.count('approved') >= minimal_approver and required_approved:
                    status = 'approved'
                else:
                    status = 'pending'
            else:
                status = 'new'
            request.request_status = status

            # Send approval accepted/refused message
            if status != old_status and status in ('approved', 'refused') and request.request_owner_id.partner_id:
                if status == 'approved':
                    body = _("The request created on %(create_date)s by %(request_owner)s has been approved.",
                            create_date=request.create_date.date(),
                            request_owner=request.request_owner_id.name)
                    subject = _("The request %(request_name)s for %(request_owner)s has been approved",
                                request_name=request.name,
                                request_owner=request.request_owner_id.name)
                else:
                    body = _("The request created on %(create_date)s by %(request_owner)s has been refused.",
                            create_date=request.create_date.date(),
                            request_owner=request.request_owner_id.name)
                    subject = _("The request %(request_name)s for %(request_owner)s has been refused",
                                request_name=request.name,
                                request_owner=request.request_owner_id.name)
                request.message_notify(
                    body=body,
                    subject=subject,
                    partner_ids=request.request_owner_id.partner_id.ids,
                )

        self.filtered_domain([('request_status', 'in', ['approved', 'refused', 'cancel'])])._cancel_activities()

    @api.depends('category_id', 'request_owner_id')
    def _compute_approver_ids(self):
        for request in self:
            users_to_category_approver = {}
            for approver in request.category_id.approver_ids:
                users_to_category_approver[approver.user_id.id] = approver

            approver_id_vals = [Command.clear()]

            if request.category_id.manager_approval:
                employee = self.env['hr.employee'].search([('user_id', '=', request.request_owner_id.id), ('company_id', '=', self.company_id.id)], limit=1)
                if employee.parent_id.user_id:
                    manager_user_id = employee.parent_id.user_id.id
                    manager_required = request.category_id.manager_approval == 'required'
                    # We set the manager sequence to be lower than all others (9) so they are the first to approve.
                    approver_id_vals.append(Command.create({
                        'user_id': manager_user_id,
                        'status': 'new',
                        'required': manager_required,
                        'sequence': 9,
                    }))
                    if manager_user_id in users_to_category_approver.keys():
                        users_to_category_approver.pop(manager_user_id)

            for user_id in users_to_category_approver:
                approver_id_vals.append(Command.create({
                    'user_id': user_id,
                    'status': 'new',
                    'required': users_to_category_approver[user_id].required,
                    'sequence': users_to_category_approver[user_id].sequence,
                }))

            request.update({'approver_ids': approver_id_vals})

    def write(self, vals):
        if not self.env.is_admin():
            for approval in self:
                if self.env.user != approval.request_owner_id:
                    continue
                # A owner cannot approve or refuse his own requests
                if vals.get('request_status') in ('approved', 'refused'):
                    raise AccessError(_("You are not allowed to approved or refused your own approval."))
                # For a processed request, the only action for the owner is to cancel the request
                if approval.request_status in ('pending', 'approved', 'refused') \
                    and (set(vals.keys()) != {'request_status'} or vals['request_status'] != 'cancel'):
                    raise AccessError(_("You must cancel and then back to draft the approval first."))

        if 'request_owner_id' in vals:
            for approval in self:
                approval.message_unsubscribe(partner_ids=approval.request_owner_id.partner_id.ids)

        res = super().write(vals)

        if 'request_owner_id' in vals:
            for approval in self:
                approval.message_subscribe(partner_ids=approval.request_owner_id.partner_id.ids)

        if 'approver_ids' in vals:
            to_resequence = self.filtered_domain([('approver_sequence', '=', True), ('request_status', '=', 'pending')])
            for approval in to_resequence:
                if not approval.approver_ids.filtered(lambda a: a.status == 'pending'):
                    approver = approval.approver_ids.filtered(lambda a: a.status == 'waiting')
                    if approver:
                        approver[0].status = 'pending'
                        approver[0]._create_activity()

        return res

    def _track_subtype(self, init_values):
        self.ensure_one()
        if 'request_status' in init_values:
            return self.env.ref('approvals.mt_approval_request_status')
        return super()._track_subtype(init_values)
```

## File: models/ir_attachment.py
```python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _
from odoo.exceptions import UserError


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.ondelete(at_uninstall=False)
    def _unlink_approved_approval_request(self):
        """
            Prevent attachment deletion for an approval request
            that is in the approved, refused or cancel state.
        """
        approval_request_ids = [attachment.res_id for attachment in self if attachment.res_model == 'approval.request' and not attachment.res_field]
        if not approval_request_ids:
            return
        approval_requests = self.env['approval.request'].browse(approval_request_ids)
        for approval_request in approval_requests:
            if approval_request.request_status in ['approved', 'refused', 'cancel']:
                raise UserError(_("You cannot unlink an attachment which is linked to a validated, refused or cancelled approval request."))
```

## File: models/mail_activity_type.py
```python
from odoo import api, models


class MailActivityType(models.Model):
    _inherit = "mail.activity.type"

    @api.model
    def _get_model_info_by_xmlid(self):
        info = super()._get_model_info_by_xmlid()
        info['approvals.mail_activity_data_approval'] = {
            'res_model': 'approval.request',
            'unlink': False,
        }
        return info
```

## File: models/mail_activity.py
```python
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.fields import Domain
from odoo.addons.mail.tools.discuss import Store


class MailActivity(models.Model):
    _inherit = "mail.activity"

    approval_request_id = fields.Many2one("approval.request", compute="_compute_approval_request_id", search="_search_approval_request_id")
    approver_id = fields.Many2one("approval.approver", compute="_compute_approver_id")

    def _search_approval_request_id(self, operator, value):
        if operator in Domain.NEGATIVE_OPERATORS:
            return NotImplemented
        if operator == 'any':
            operator = 'in'
            if isinstance(value, Domain):
                value = self.env['approval.request']._search(value)
        activity_type_approval_id = self.env.ref("approvals.mail_activity_data_approval")
        return [
            [("res_model", "=", "approval.request")],
            [("activity_type_id", "=", activity_type_approval_id)],
            [("res_id", operator, value)]
        ]

    @api.depends("activity_type_id", "res_id", "res_model")
    def _compute_approval_request_id(self):
        activity_type_approval_id = self.env.ref("approvals.mail_activity_data_approval")
        for activity in self:
            if activity["res_model"] == "approval.request" and activity.activity_type_id == activity_type_approval_id:
                activity.approval_request_id = self.env["approval.request"].browse(activity["res_id"])
            else:
                activity.approval_request_id = None

    @api.depends("user_id", "approval_request_id.approver_ids.user_id")
    def _compute_approver_id(self):
        for activity in self:
            activity.approver_id = activity.approval_request_id.approver_ids.filtered(
                lambda approver: activity.user_id == approver.user_id
            )

    def _to_store_defaults(self, target):
        return super()._to_store_defaults(target) + [Store.One("approver_id", ["status"])]
```

## File: report/approval_request_report.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="action_report_approval_request" model="ir.actions.report">
        <field name="name">Approval Request</field>
        <field name="model">approval.request</field>
        <field name="report_type">qweb-pdf</field>
        <field name="report_name">approvals.report_approval_request</field>
        <field name="report_file">approvals.report_approval_request</field>
        <field name="print_report_name">'Approval - %s' % object.name</field>
        <field name="binding_model_id" ref="model_approval_request"/>
        <field name="binding_type">report</field>
    </record>
</odoo>
```

## File: security/approval_security.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record model="res.groups.privilege" id="res_groups_privilege_approvals">
        <field name="name">Approvals</field>
        <field name="sequence">9</field>
        <field name="category_id" ref="base.module_category_human_resources"/>
    </record>

    <record id="group_approval_user" model="res.groups">
        <field name="name">Officer: Approve all requests</field>
        <field name="sequence">10</field>
        <field name="privilege_id" ref="res_groups_privilege_approvals"/>
        <field name="implied_ids" eval="[(6, 0, [ref('base.group_user')])]"/>
        <field name="comment">The user will be able to access all requests and approve/refuse them.</field>
    </record>

    <record id="group_approval_manager" model="res.groups">
        <field name="name">Administrator</field>
        <field name="sequence">20</field>
        <field name="comment">The user will have access to the approvals configuration.</field>
        <field name="privilege_id" ref="res_groups_privilege_approvals"/>
        <field name="implied_ids" eval="[(4, ref('group_approval_user'))]"/>
    </record>

    <data noupdate="1">
        <!-- Regular User -->
        <record id="approval_request_request_approver_rule" model="ir.rule">
            <field name="name">Approval Request: request approver rule</field>
            <field name="model_id" ref="model_approval_request"/>
            <field name="groups" eval="[(4, ref('base.group_user'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="1"/>
            <field name="perm_unlink" eval="0"/>
            <field name="domain_force">['|', '|',
                                        ('request_owner_id', '=', user.id),
                                        ('approver_ids.user_id','=', user.id),
                                        '&amp;',
                                        ('category_id.manager_approval', 'in', ['approver', 'required']),
                                        ('request_owner_id.parent_id.user_id', '=', user.id)]</field>
        </record>

        <record id="approval_request_product_line_approver_rule" model="ir.rule">
            <field name="name">Approval Product Line: request approver rule</field>
            <field name="model_id" ref="model_approval_product_line"/>
            <field name="groups" eval="[(4, ref('base.group_user'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="1"/>
            <field name="perm_unlink" eval="1"/>
            <field name="domain_force">['|', '|',
                                        ('approval_request_id.request_owner_id', '=', user.id),
                                        ('approval_request_id.approver_ids.user_id','=', user.id),
                                        '&amp;',
                                        ('approval_request_id.category_id.manager_approval', 'in', ['approver', 'required']),
                                        ('approval_request_id.request_owner_id.parent_id.user_id', '=', user.id)]</field>
        </record>

        <record id="approval_request_unlink_request_owner_rule" model="ir.rule">
            <field name="name">Approval Request: unlink request owner rule</field>
            <field name="model_id" ref="model_approval_request"/>
            <field name="groups" eval="[(4, ref('base.group_user'))]"/>
            <field name="perm_read" eval="0"/>
            <field name="perm_write" eval="0"/>
            <field name="perm_create" eval="0"/>
            <field name="perm_unlink" eval="1"/>
            <field name="domain_force">[('request_owner_id', '=', user.id), ('request_status', 'in', ['cancel', 'new'])]</field>
        </record>

        <record id="approval_approver_user_read_own" model="ir.rule">
            <field name="name">Approval Approver: read own request</field>
            <field name="model_id" ref="model_approval_approver"/>
            <field name="groups" eval="[(4, ref('base.group_user'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="0"/>
            <field name="perm_create" eval="0"/>
            <field name="perm_unlink" eval="0"/>
            <field name="domain_force">['|', ('request_id.request_owner_id', '=', user.id), ('user_id', '=', user.id)]</field>
        </record>

        <record id="approval_approver_user_change_own" model="ir.rule">
            <field name="name">Approval Approver: change own</field>
            <field name="model_id" ref="model_approval_approver"/>
            <field name="groups" eval="[(4, ref('base.group_user'))]"/>
            <field name="perm_read" eval="0"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="0"/>
            <field name="perm_unlink" eval="0"/>
            <field name="domain_force">[('user_id', '=', user.id)]</field>
        </record>

        <!-- Approval User -->
        <record id="approval_request_user" model="ir.rule">
            <field name="name">Approval Request: user</field>
            <field name="model_id" ref="model_approval_request"/>
            <field name="groups" eval="[(4, ref('group_approval_user'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="1"/>
            <field name="perm_unlink" eval="0"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <record id="approval_request_user_unlink" model="ir.rule">
            <field name="name">Approval Request: user unlink</field>
            <field name="model_id" ref="model_approval_request"/>
            <field name="groups" eval="[(4, ref('group_approval_user'))]"/>
            <field name="perm_read" eval="0"/>
            <field name="perm_write" eval="0"/>
            <field name="perm_create" eval="0"/>
            <field name="perm_unlink" eval="1"/>
            <field name="domain_force">[('request_status','=','cancel')]</field>
        </record>

        <record id="approval_product_line_user" model="ir.rule">
            <field name="name">Approval Product Line: user</field>
            <field name="model_id" ref="model_approval_product_line"/>
            <field name="groups" eval="[(4, ref('group_approval_user'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="1"/>
            <field name="perm_unlink" eval="0"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <record id="approval_product_line_user_unlink" model="ir.rule">
            <field name="name">Approval Product Line: user unlink</field>
            <field name="model_id" ref="model_approval_product_line"/>
            <field name="groups" eval="[(4, ref('group_approval_user'))]"/>
            <field name="perm_read" eval="0"/>
            <field name="perm_write" eval="0"/>
            <field name="perm_create" eval="0"/>
            <field name="perm_unlink" eval="1"/>
            <field name="domain_force">[('approval_request_id.request_status','=','cancel')]</field>
        </record>

        <record id="approval_approver_manager" model="ir.rule">
            <field name="name">Approval Approver: manage all</field>
            <field name="model_id" ref="model_approval_approver"/>
            <field name="groups" eval="[(4, ref('group_approval_user'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="1"/>
            <field name="perm_unlink" eval="0"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <record id="approval_approver_manager_unlink" model="ir.rule">
            <field name="name">Approval Approver: unlink unapproved</field>
            <field name="model_id" ref="model_approval_approver"/>
            <field name="groups" eval="[(4, ref('group_approval_user'))]"/>
            <field name="perm_read" eval="0"/>
            <field name="perm_write" eval="0"/>
            <field name="perm_create" eval="0"/>
            <field name="perm_unlink" eval="1"/>
            <field name="domain_force">[('request_id.request_status', 'in', ['new', 'pending', 'cancel'])]</field>
        </record>

        <!-- Approval Administrator -->
        <record id="approval_request_manager" model="ir.rule">
            <field name="name">Approval Request: manager</field>
            <field name="model_id" ref="model_approval_request"/>
            <field name="groups" eval="[(4, ref('group_approval_manager'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="1"/>
            <field name="perm_unlink" eval="1"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <record id="approval_approver_manager" model="ir.rule">
            <field name="name">Approval Approver: manager</field>
            <field name="model_id" ref="model_approval_approver"/>
            <field name="groups" eval="[(4, ref('group_approval_manager'))]"/>
            <field name="perm_read" eval="1"/>
            <field name="perm_write" eval="1"/>
            <field name="perm_create" eval="1"/>
            <field name="perm_unlink" eval="1"/>
            <field name="domain_force">[(1, '=', 1)]</field>
        </record>

        <!-- Multi-company rules -->
        <record model="ir.rule" id="approval_request_rule">
            <field name="name">approval_request multi-company</field>
            <field name="model_id" search="[('model','=','approval.request')]" model="ir.model"/>
            <field name="domain_force">[('company_id', 'in', company_ids)]</field>
        </record>
        <record model="ir.rule" id="approval_category_rule">
            <field name="name">approval_category multi-company</field>
            <field name="model_id" search="[('model','=','approval.category')]" model="ir.model"/>
            <field name="domain_force">[('company_id', 'in', company_ids)]</field>
        </record>
        <record model="ir.rule" id="approval_approver_rule">
            <field name="name">approval_approver multi-company</field>
            <field name="model_id" search="[('model','=','approval.approver')]" model="ir.model"/>
            <field name="domain_force">[('company_id', 'in', company_ids)]</field>
        </record>
        <record model="ir.rule" id="approval_product_line_rule">
            <field name="name">approval_product_line multi-company</field>
            <field name="model_id" search="[('model','=','approval.product.line')]" model="ir.model"/>
            <field name="domain_force">[('company_id', 'in', company_ids)]</field>
        </record>
    </data>

    <function model="ir.rule" name="write">
        <value eval="[ref('approvals.approval_request_unlink_request_owner_rule')]"/>
        <value eval="{'domain_force': '[(\'request_owner_id.id\', \'=\', user.id), (\'request_status\', \'in\', (\'new\', \'cancel\'))]'}"/>
    </function>
</odoo>
```

## File: security/ir.model.access.csv
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_approval_request,access_approval_request,model_approval_request,base.group_user,1,1,1,1
access_approval_request_user,access_approval_request,model_approval_request,group_approval_user,1,1,1,1
access_approval_request_manager,access_approval_request,model_approval_request,group_approval_manager,1,1,1,1
access_approval_category,access_approval_category,model_approval_category,base.group_user,1,0,0,0
access_approval_category_user,access_approval_category,model_approval_category,group_approval_user,1,0,0,0
access_approval_category_manager,access_approval_category,model_approval_category,group_approval_manager,1,1,1,1
access_approval_category_approver,access_approval_category_approver,model_approval_category_approver,base.group_user,1,0,0,0
access_approval_category_approver_user,access_approval_category_approver,model_approval_category_approver,group_approval_user,1,0,0,0
access_approval_category_approver_manager,access_approval_category_approver,model_approval_category_approver,group_approval_manager,1,1,1,1
access_approval_approver,access_approval_approver,model_approval_approver,base.group_user,1,1,0,0
access_approval_approver_user,access_approval_approver,model_approval_approver,group_approval_user,1,1,1,1
access_approval_approver_manager,access_approval_approver,model_approval_approver,group_approval_manager,1,1,1,1
access_approval_product_line_user,access_approval_product_line,model_approval_product_line,base.group_user,1,1,1,1
access_approval_product_line_manager,access_approval_product_line,model_approval_product_line,group_approval_manager,1,1,1,1
```

## File: static/description/icon.svg
```xml
<svg width="50" height="50" viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg"><path d="M28 16c0 5.523-4.477 10-10 10S8 21.523 8 16 12.477 6 18 6s10 4.477 10 10Z" fill="#1AD3BB"/><path d="M43 24a5 5 0 1 1-10 0 5 5 0 0 1 10 0Zm-27 7h26a4 4 0 0 1 4 4v5a4 4 0 0 1-4 4H16V31Z" fill="#005E7A"/><path d="M4 31h16c7.18 0 13 5.82 13 13H17C9.82 44 4 38.18 4 31Z" fill="#1AD3BB"/><path d="M23.549 12.128 22.425 11l-5.532 5.556-3.319-3.335-1.123 1.129a1.552 1.552 0 0 0 0 2.188L16.892 21l6.657-6.685a1.55 1.55 0 0 0 0-2.187Z" fill="#fff"/></svg>
```

## File: static/src/common/activity_model_patch.js
```javascript
import { Activity } from "@mail/core/common/activity_model";
import { fields } from "@mail/core/common/record";

import { patch } from "@web/core/utils/patch";

patch(Activity.prototype, {
    setup() {
        super.setup(...arguments);
        this.approver_id = fields.One("approval.approver");
    },
});
```

## File: static/src/common/approver_model.js
```javascript
import { Record } from "@mail/core/common/record";

export class ApprovalApprover extends Record {
    static _name = "approval.approver";
    static id = "id";
    /** @type {number} */
    id;
    /** @type {"new"|"pending"|"waiting"|"approved"|"refused"|"cancel"} */
    status;
}

ApprovalApprover.register();
```

## File: static/src/scss/approvals.scss
```scss
.o_approval_kanban_avatar {
    .o_avatar {
        gap: 0.375rem;
    }
}
```

## File: static/src/views/kanban/approvals_category_kanban_controller.js
```javascript
import { _t } from "@web/core/l10n/translation";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { useService } from "@web/core/utils/hooks";

import { KanbanController } from "@web/views/kanban/kanban_controller";
import { KanbanRenderer } from "@web/views/kanban/kanban_renderer";

export class ApprovalCategoryKanbanController extends KanbanController {
    async setup() {
        super.setup();
        this.action = useService("action");
    }

    OpenNewApprovalRequest() {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "approval.request",
            views: [[false, "form"]],
            target: "current",
        });
    }
}

export class ApprovalKanbanRenderer extends KanbanRenderer {
    async archiveRecord(record, active) {
        if (active) {
            this.dialog.add(ConfirmationDialog, {
                body: _t("Are you sure that you want to archive this record?"),
                confirmLabel: _t("Archive"),
                confirm: () => {
                    record.archive();
                    this.props.list.load(); 
                },
                cancel: () => {},
            });
        } else {
            record.unarchive();
            this.props.list.load();
        }
    }
}
```

## File: static/src/views/kanban/approvals_category_kanban_controller.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates xml:space="preserve">
    <t t-name="approvals.ApprovalsCategoryKanbanView.Buttons">
        <button type="button" class="btn btn-primary" t-on-click="OpenNewApprovalRequest">
            New Request
        </button>
    </t>
</templates>
```

## File: static/src/views/kanban/approvals_category_kanban_view.js
```javascript
import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view";

import { ApprovalKanbanRenderer, ApprovalCategoryKanbanController } from "./approvals_category_kanban_controller";

export const approvalsCategoryKanbanView = {
    ...kanbanView,
    Controller: ApprovalCategoryKanbanController,
    Renderer: ApprovalKanbanRenderer,
    buttonTemplate: "approvals.ApprovalsCategoryKanbanView.Buttons",
};

registry.category("views").add("approvals_category_kanban", approvalsCategoryKanbanView);
```

## File: static/src/web/activity_list_popover_item_patch.js
```javascript
import { Approval } from "@approvals/web/approval";

import { ActivityListPopoverItem } from "@mail/core/web/activity_list_popover_item";

import { patch } from "@web/core/utils/patch";

Object.assign(ActivityListPopoverItem.components, { Approval });

patch(ActivityListPopoverItem.prototype, {
    get hasEditButton() {
        if (this.props.activity.approval) {
            return false;
        }
        return super.hasEditButton;
    },
    get hasMarkDoneButton() {
        if (this.props.activity.approval) {
            return false;
        }
        return super.hasMarkDoneButton;
    },
});
```

## File: static/src/web/activity_list_popover_item_patch.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates xml:space="preserve">

    <t t-inherit="mail.ActivityListPopoverItem" t-inherit-mode="extension">
        <xpath expr="//button[hasclass('o-mail-ActivityListPopoverItem-markAsDone')]" position="after">
            <Approval t-if="props.activity.approval" activity="this.props.activity" onChange="this.props.onActivityChanged"/>
        </xpath>
    </t>

</templates>
```

## File: static/src/web/activity_patch.js
```javascript
import { Activity } from "@mail/core/web/activity";

import { Approval } from "@approvals/web/approval";

Object.assign(Activity.components, { Approval });
```

## File: static/src/web/activity_patch.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates xml:space="preserve">

    <t t-inherit="mail.Activity" t-inherit-mode="extension">
        <xpath expr="//t[@name='tools']" position="replace">
            <Approval t-if="props.activity.approver_id" activity="props.activity" onChange="props.reloadParentView"/>
            <t t-else="">$0</t>
        </xpath>
    </t>

</templates>
```

## File: static/src/web/approval.js
```javascript
import { Component } from "@odoo/owl";

import { useService } from "@web/core/utils/hooks";

/**
 * @typedef {Object} Props
 * @property {import("models").Activity} activity
 * @extends {Component<Props, Env>}
 */
export class Approval extends Component {
    static template = "approvals.Approval";
    static props = {
        activity: Object,
        onChange: Function,
    };

    setup() {
        this.store = useService("mail.store");
    }

    async onClickApprove() {
        await this.env.services.orm.call("approval.approver", "action_approve", [
            this.props.activity.approver_id.id,
        ]);
        this.props.activity.remove();
        this.props.onChange();
    }

    async onClickRefuse() {
        await this.env.services.orm.call("approval.approver", "action_refuse", [
            this.props.activity.approver_id.id,
        ]);
        this.props.activity.remove();
        this.props.onChange();
    }
}
```

## File: static/src/web/approval.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<templates xml:space="preserve">

    <t t-name="approvals.Approval">
        <div t-if="props.activity.approver_id.status === 'pending'">
            <button class="btn btn-success btn-link ps-0 pt-0" t-on-click="onClickApprove">
                <i class="fa fa-check"/> Approve
            </button>
            <button class="btn btn-danger btn-link pt-0" t-on-click="onClickRefuse">
                <i class="fa fa-times"/> Refuse
            </button>
        </div>
    </t>

</templates>
```

## File: static/tests/mock_server/mock_models/approval_approver.js
```javascript
import { models } from "@web/../tests/web_test_helpers";

export class ApprovalApprover extends models.ServerModel {
    _name = "approval.approver";

    action_approve() {
        return true;
    }

    action_refuse() {
        return true;
    }
}
```

## File: static/tests/mock_server/mock_models/approval_request.js
```javascript
import { models } from "@web/../tests/web_test_helpers";

export class ApprovalRequest extends models.ServerModel {
    _name = "approval.request";
    _views = {
        form: /* xml */ `
            <form>
                <chatter/>
            </form>`,
    };
}
```

## File: static/tests/mock_server/mock_models/mail_activity.js
```javascript
import { mailModels } from "@mail/../tests/mail_test_helpers";

export class MailActivity extends mailModels.MailActivity {
    /** @param {number[]} ids */
    _to_store(store) {
        super._to_store(...arguments);
        for (const activity of this._filter([
            ["id", "in", this.map((activity) => activity.id)],
            ["res_model", "=", "approval.request"],
        ])) {
            // check on activity type being approval not done here for simplicity
            const [approver_id] = this.env["approval.approver"]._filter([
                ["request_id", "=", activity.res_id],
                ["user_id", "=", activity.user_id],
            ]);
            if (approver_id) {
                store._add_record_fields(this.browse(activity.id), {
                    approver_id: { id: approver_id.id, status: approver_id.status },
                });
            }
        }
    }
}
```

## File: static/tests/tours/approvals.js
```javascript
import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("approvals_tour", {
    url: "/odoo",
    steps: () => [
        {
            trigger: '.o_app[data-menu-xmlid="approvals.approvals_menu_root"]',
            content: "open approvals app",
            run: "click",
        },
        {
            trigger: "button.oe_kanban_action:first",
            content: "create new request",
            run: "click",
        },
        {
            trigger: '.o_field_widget[name="name"] input',
            content: "give name",
            run: "edit Business Trip To Berlin",
        },
        {
            trigger: '.o_field_widget[name="date_start"] input',
            content: "give start date",
            run: "edit 12/13/2018 13:00:00",
        },
        {
            trigger: '.o_field_widget[name="date_end"] input',
            content: "give end date",
            run: "edit 12/20/2018 13:00:00",
        },
        {
            trigger: '.o_field_widget[name="location"] input',
            content: "give location",
            run: "edit Berlin, Schulz Hotel",
        },
        {
            trigger: 'div[name="reason"] .odoo-editor-editable',
            content: "give description",
            run: "editor (We need to go, because reason (and also for beer)))",
        },
        {
            trigger: 'a:contains("Approver(s)"):first',
            content: "open approvers page",
            run: "click",
        },
        {
            trigger: ".o_field_x2many_list_row_add > a",
            content: "add an approver",
            run: "click",
        },
        {
            content: "select an approver",
            trigger: ".o_selected_row .o_input_dropdown input",
            run: "edit Marc",
        },
        {
            isActive: ["auto"],
            trigger: ".ui-autocomplete > li > a:contains(Marc)",
            run: "click",
        },
        {
            trigger: ".o_form_button_save",
            content: "save the request",
            run: "click",
        },
        {
            trigger: "button[name=action_confirm]:enabled",
            content: "confirm the request",
            run: "click",
        },
        {
            trigger: ".o-mail-Activity button:contains('Approve')",
            content: "approve the request via activity",
            run: "click",
        },
        {
            trigger: 'button[name="action_withdraw"]',
            content: "withdraw approver",
            run: "click",
        },
        {
            trigger: 'button[name="action_refuse"]',
            content: "refuse request",
            run: "click",
        },
        {
            trigger: 'button[aria-checked="true"][data-value="refused"]',
            content: "wait the request status compute",
        },
        {
            trigger: 'button[name="action_cancel"]',
            content: "cancel request",
            run: "click",
        },
        {
            trigger: 'button[name="action_draft"]',
            content: "back the request to draft",
            run: "click",
        },
        {
            trigger: "button[name=action_confirm]:enabled",
            content: "confirm the request again",
            run: "click",
        },
        {
            trigger: 'button[name="action_approve"]',
            content: "approve request",
            run: "click",
        },
        {
            trigger: 'button[name="action_withdraw"]',
            content: "wait the the request to be approved",
        },
    ],
});
```

## File: static/tests/activity_patch.test.js
```javascript
import { describe, expect, test } from "@odoo/hoot";
import { Deferred } from "@odoo/hoot-mock";

import { defineApprovalsModels } from "@approvals/../tests/approvals_test_helpers";
import {
    click,
    contains,
    openFormView,
    start,
    startServer,
} from "@mail/../tests/mail_test_helpers";
import { asyncStep, onRpc, serverState, waitForSteps } from "@web/../tests/web_test_helpers";

describe.current.tags("desktop");
defineApprovalsModels();

test("activity with approval to be made by logged user", async () => {
    const pyEnv = await startServer();
    const requestId = pyEnv["approval.request"].create({});
    pyEnv["approval.approver"].create({
        request_id: requestId,
        status: "pending",
        user_id: serverState.userId,
    });
    pyEnv["mail.activity"].create({
        can_write: true,
        res_id: requestId,
        res_model: "approval.request",
        user_id: serverState.userId,
    });
    await start();
    await openFormView("approval.request", requestId);
    await contains(".o-mail-Activity");
    await contains(".o-mail-Activity-sidebar");
    await contains(".o-mail-Activity-user");
    await contains(".o-mail-Activity-note", { count: 0 });
    await contains(".o-mail-Activity-details", { count: 0 });
    await contains(".o-mail-Activity-mailTemplates", { count: 0 });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Edit" });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Cancel" });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Mark Done" });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Upload Document" });
    await contains(".o-mail-Activity button", { text: "Approve" });
    await contains(".o-mail-Activity button", { text: "Refuse" });
});

test("activity with approval to be made by another user", async () => {
    const pyEnv = await startServer();
    const requestId = pyEnv["approval.request"].create({});
    const userId = pyEnv["res.users"].create({
        partner_id: pyEnv["res.partner"].create({
            name: "Mike",
        }),
    });
    pyEnv["approval.approver"].create({
        request_id: requestId,
        status: "pending",
        user_id: userId,
    });
    pyEnv["mail.activity"].create({
        can_write: true,
        res_id: requestId,
        res_model: "approval.request",
        user_id: userId,
    });
    await start();
    await openFormView("approval.request", requestId);
    await contains(".o-mail-Activity");
    await contains(".o-mail-Activity-sidebar");
    await contains(".o-mail-Activity-user");
    await contains(".o-mail-Activity-note", { count: 0 });
    await contains(".o-mail-Activity-details", { count: 0 });
    await contains(".o-mail-Activity-mailTemplates", { count: 0 });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Edit" });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Cancel" });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Mark Done" });
    await contains(".o-mail-Activity .btn", { count: 0, text: "Upload Document" });
    await contains(".o-mail-Activity button", { count: 1, text: "Approve" });
    await contains(".o-mail-Activity button", { count: 1, text: "Refuse" });
});

test("approve approval", async () => {
    const pyEnv = await startServer();
    const requestId = pyEnv["approval.request"].create({});
    pyEnv["approval.approver"].create({
        request_id: requestId,
        status: "pending",
        user_id: serverState.userId,
    });
    pyEnv["mail.activity"].create({
        can_write: true,
        res_id: requestId,
        res_model: "approval.request",
        user_id: serverState.userId,
    });
    const def = new Deferred();
    onRpc("approval.approver", "action_approve", (args) => {
        expect(args.args.length).toBe(1);
        expect(args.args[0]).toBe(requestId);
        asyncStep("action_approve");
        def.resolve();
    });
    await start();
    await openFormView("approval.request", requestId);
    await click(".o-mail-Activity button", { text: "Approve" });
    await def;
    await waitForSteps(["action_approve"]);
});

test("refuse approval", async () => {
    const pyEnv = await startServer();
    const requestId = pyEnv["approval.request"].create({});
    pyEnv["approval.approver"].create({
        request_id: requestId,
        status: "pending",
        user_id: serverState.userId,
    });
    pyEnv["mail.activity"].create({
        can_write: true,
        res_id: requestId,
        res_model: "approval.request",
        user_id: serverState.userId,
    });
    const def = new Deferred();
    onRpc("approval.approver", "action_refuse", (args) => {
        expect(args.args.length).toBe(1);
        expect(args.args[0]).toBe(requestId);
        asyncStep("action_refuse");
        def.resolve();
    });
    await start();
    await openFormView("approval.request", requestId);
    await click(".o-mail-Activity button", { text: "Refuse" });
    await def;
    await waitForSteps(["action_refuse"]);
});
```

## File: static/tests/approvals_test_helpers.js
```javascript
import { defineModels } from "@web/../tests/web_test_helpers";
import { mailModels } from "@mail/../tests/mail_test_helpers";
import { ApprovalRequest } from "@approvals/../tests/mock_server/mock_models/approval_request";
import { ApprovalApprover } from "@approvals/../tests/mock_server/mock_models/approval_approver";
import { MailActivity } from "@approvals/../tests/mock_server/mock_models/mail_activity";

export function defineApprovalsModels() {
    return defineModels(approvalsModels);
}

export const approvalsModels = {
    ...mailModels,
    ApprovalRequest,
    ApprovalApprover,
    MailActivity
};
```

## File: views/approval_category_approver_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <!-- Approval Category Approver -->
    <record id="approval_category_approver_view_tree" model="ir.ui.view">
        <field name="name">approval.category.approver.view.list</field>
        <field name="model">approval.category.approver</field>
        <field name="arch" type="xml">
            <list editable="bottom">
                <field name="existing_user_ids" column_invisible="True"/>
                <field name="company_id" column_invisible="True"/>
                <field name="sequence" widget="handle" />
                <field name="user_id" widget="many2one_avatar_user" options="{'no_create': True}"/>
                <field name="required"/>
            </list>
        </field>
    </record>
</odoo>
```

## File: views/approval_category_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="approval_category_action_new_request" model="ir.actions.act_window">
        <field name="name">Dashboard</field>
        <field name="path">approvals</field>
        <field name="res_model">approval.category</field>
        <field name="view_mode">kanban</field>
    </record>

    <record id="approval_category_action" model="ir.actions.act_window">
        <field name="name">Approval Categories</field>
        <field name="res_model">approval.category</field>
        <field name="view_mode">list,form</field>
    </record>

    <record id="approval_request_action_to_review_category" model="ir.actions.act_window">
        <field name="name">Approvals to review</field>
        <field name="res_model">approval.request</field>
        <field name="view_mode">list,form,kanban</field>
        <field name="domain">[('approver_ids.user_id', '=', uid), ('request_status', '=', 'pending'), ('category_id', '=', active_id)]</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                No new approvals to review 
            </p>
        </field>

    </record>

    <record id="approval_category_view_tree" model="ir.ui.view">
        <field name="name">approval.category.view.list</field>
        <field name="model">approval.category</field>
        <field name="priority">10</field>
        <field name="arch" type="xml">
            <list>
                <field name="sequence" widget="handle" />
                <field name="name"/>
                <field name="company_id" groups="base.group_multi_company" optional="show"/>
            </list>
        </field>
    </record>

    <record id="approval_category_view_search" model="ir.ui.view">
        <field name="name">approval.category.search</field>
        <field name="model">approval.category</field>
        <field name="priority">10</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <separator/>
                <filter name="archived" string="Archived" domain="[('active', '=', False)]"/>
            </search>
        </field>
    </record>

    <record id="approval_category_view_form" model="ir.ui.view">
        <field name="name">approval.category.view.form</field>
        <field name="model">approval.category</field>
        <field name="priority">10</field>
        <field name="arch" type="xml">
            <form>
                <sheet>
                    <widget name="web_ribbon" title="Archived" bg_color="text-bg-danger" invisible="active"/>
                    <field name="image" widget="image" class="oe_avatar" options='{"preview_image": "image", "size": [80, 80]}'/>
                    <div class="oe_title">
                        <label for="name" string="Approval Category"/>
                        <h1>
                            <field name="name" placeholder="e.g. Procurement"/>
                        </h1>
                    </div>
                    <group>
                        <field name="description"/>
                        <field name="approval_type" invisible="1"/>
                        <field name="automated_sequence"/>
                        <field name="sequence_code" invisible="not automated_sequence" required="automated_sequence"/>
                        <field name="company_id" options="{'no_create': True}" groups="base.group_multi_company"/>
                    </group>
                    <notebook>
                        <page string="Options" name="options">
                            <group>
                                <group string="Fields" name="option_settings">
                                    <field name="active" invisible="1"/>
                                    <field name="requirer_document" string="Document" widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_partner" string="Contact" widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_date" string="Date" widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_period" string="Period" widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_product" string="Product" force_save="1"
                                        widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_quantity" string="Quantity" widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_amount" string="Amount" widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_reference" string="Reference" widget="radio" options="{'horizontal': true}"/>
                                    <field name="has_payment_method" string="Payment" widget="radio" options="{'horizontal': true}" invisible="1"/>
                                    <field name="has_location" string="Location" widget="radio" options="{'horizontal': true}"/>
                                </group>
                                <group string="Approvers" name="approvers">
                                    <field name="manager_approval"/>
                                    <label for="approver_ids" string="Approvers"/>
                                    <field name="approver_ids" colspan="2" nolabel="1"/>
                                    <field name="approver_sequence" invisible="approval_minimum == 0"/>
                                    <field name="approval_minimum"/>
                                    <field name="invalid_minimum" invisible="1"/>
                                    <div class="text-warning" colspan="2" invisible="not invalid_minimum">
                                        <span class="fa fa-warning" title="Invalid minimum approvals"/><field name="invalid_minimum_warning" nolabel="1"/>
                                    </div>
                                </group>
                            </group>
                        </page>
                    </notebook>
                </sheet>
            </form>
        </field>
    </record>

    <record id="action_open_approval_category" model="ir.actions.server">
        <field name="name">Open Approval Category</field>
        <field name="model_id" ref="model_approval_category"/>
        <field name="state">code</field>
        <field name="code">
            action = {
                "type": "ir.actions.act_window",
                "res_model": "approval.category",
                "views": [[False, "form"]],
                "target": "new",
                "res_id": records.id,
                "name": "Approval Settings",
            }
        </field>
    </record>

    <record id="approval_category_view_kanban" model="ir.ui.view">
        <field name="name">approval.category.views.kanban</field>
        <field name="model">approval.category</field>
        <field name="arch" type="xml">
            <kanban create="false" can_open="0" class="o_modules_kanban" js_class="approvals_category_kanban">
                <field name="active"/>
                <templates>
                    <t t-name="menu" groups="approvals.group_approval_user">
                        <a t-if="widget.editable"
                            role="menuitem"
                            type="action"
                            name="%(approvals.action_open_approval_category)d"
                            class="dropdown-item">Edit</a>
                        <a t-if="record.active.raw_value"
                            role="menuitem" 
                            type="archive"
                            class="dropdown-item">Archive</a>
                        <a t-if="!record.active.raw_value"
                            role="menuitem"
                            type="unarchive"
                            class="dropdown-item">Unarchive</a>
                    </t>
                    <t t-name="card" class="flex-row">
                        <widget name="web_ribbon" title="Archived" bg_color="text-bg-danger" invisible="active"/>
                        <aside>
                            <field name="image" widget="image" class="mt-2"/>
                        </aside>
                        <main class="ms-4">
                            <field name="name" class="fw-bold fs-5"/>
                            <field name="description" class="text-muted lh-1 mb-1 mt-1"/>
                            <footer t-if="!selection_mode">
                                <button type="object" class="btn btn-primary btn-sm" name="create_request" context="{'category_id':id}">New Request</button>
                                <button type="action" class="btn btn-sm btn-secondary ms-auto" name="%(approvals.approval_request_action_to_review_category)d" groups="approvals.group_approval_user">To Review: <field name="request_to_validate_count"/></button>
                            </footer>
                        </main>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>
</odoo>
```

## File: views/approval_product_line_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="approval_product_line_view_tree_independent" model="ir.ui.view">
        <field name="name">approval.product.line.view.list</field>
        <field name="model">approval.product.line</field>
        <!-- This priority should be lower than the regular list view,
        so studio takes it instead of the regular view,
        which is embedded in a form view by default -->
        <field name="priority">10</field>
        <field name="arch" type="xml">
            <list editable="bottom" string="Products">
                <field name="approval_request_id"/>
                <field name="company_id" column_invisible="True"/>
                <field name="product_id"/>
                <field name="description"/>
                <field name="quantity"/>
                <field name="product_uom_id" groups="uom.group_uom" widget="many2one_uom"
                    options="{'no_create': True, 'no_open': True}"/>
            </list>
        </field>
    </record>

    <record id="approval_product_line_view_tree" model="ir.ui.view">
        <field name="name">approval.product.line.view.list</field>
        <field name="model">approval.product.line</field>
        <field name="priority">15</field>
        <field name="arch" type="xml">
            <list editable="bottom" string="Products">
                <field name="company_id" column_invisible="True"/>
                <field name="product_id" required="parent.has_product == 'required'" context="{'search_default_filter_to_purchase': 1}"/>
                <field name="description"/>
                <field name="quantity" column_invisible="parent.has_quantity == 'no'" required="parent.has_quantity == 'required' and parent.request_status != 'new'"/>
                <field name="product_uom_id" groups="uom.group_uom" widget="many2one_uom"
                    options="{'no_create': True, 'no_open': True}"/>
            </list>
        </field>
    </record>

    <record id="approval_product_line_view_form" model="ir.ui.view">
        <field name="name">approval.product.line.view.form</field>
        <field name="model">approval.product.line</field>
        <field name="arch" type="xml">
            <form string="Products">
                <sheet>
                    <group>
                        <field name="company_id" invisible="1"/>
                        <field name="product_id"/>
                        <field name="description"/>
                        <field name="quantity"/>
                        <field name="product_uom_id" groups="uom.group_uom" widget="many2one_uom"/>
                    </group>
                </sheet>
            </form>
        </field>
    </record>

    <record id="approval_product_kanban_mobile_view" model="ir.ui.view">
        <field name="name">approval.product.kanban.mobile</field>
        <field name="model">approval.product.line</field>
        <field name="priority">15</field>
        <field name="arch" type="xml">
            <kanban editable="bottom" string="Products">
                <templates>
                        <t t-name="card" class="d-flex justify-content-between">
                            <field name="product_id" class="fw-bolder fs-5"/>
                            <field name="quantity" class="fw-bolder fs-5"/>
                        </t>
                </templates>
            </kanban>
        </field>
    </record>
</odoo>
```

## File: views/approval_products_views.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <record id="product_template_action" model="ir.actions.act_window">
        <field name="name">Products</field>
        <field name="res_model">product.template</field>
        <field name="search_view_id" ref="product.product_template_search_view"/>
        <field name="view_mode">kanban,list,form</field>
        <field name="context">{'search_default_filter_to_purchase': 1}</field>
        <field name="help" type="html">
          <p class="o_view_nocontent_smiling_face">
            No product found. Let's create one!
          </p><p>
            Define the components and finished products you wish to use in
            bill of materials and manufacturing orders.
          </p>
        </field>
    </record>
    <record id="product_product_action" model="ir.actions.act_window">
        <field name="name">Product Variants</field>
        <field name="res_model">product.product</field>
        <field name="view_mode">list,form,kanban,activity</field>
        <field name="search_view_id" ref="product.product_template_search_view"/>
        <field name="context">{'search_default_filter_to_purchase': 1}</field>
        <field name="help" type="html">
          <p class="o_view_nocontent_smiling_face">
            Create a new product variant
          </p><p>
            You must define a product for everything you sell or purchase,
            whether it's a storable product, a consumable or a service.
          </p>
        </field>
    </record>
</odoo>
```

## File: views/approval_request_template.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <template id="report_aprroval_request_document">
        <t t-call="web.external_layout">
            <t t-set="o" t-value="o.with_context(lang=o.partner_id.lang)"/>
            <h5 class="mt-2" t-field="o.category_id.name">Test Category</h5>
            <div class="row mt-4">
                <div class="col-6">
                    <div class="d-flex">
                        <h6 class="col-3 fw-bold">Request By:</h6>
                        <h6 t-field="o.request_owner_id">Marc Demo</h6>
                    </div>
                    <div class="d-flex">
                        <h6 class="col-3 fw-bold">Approvers:</h6>
                        <div>
                            <h6 t-foreach="o.approver_ids" t-as="approver_id" class="mb-2">
                                <span t-field="approver_id.user_id.name">Mitchell Admin</span>
                                <span t-if="approver_id.status == 'approved'">(&#10004;)</span>
                            </h6>
                        </div>
                    </div>
                    <div class="d-flex">
                        <h6 class="col-3 fw-bold">Status:</h6>
                        <h6 t-field="o.request_status">Approved</h6>
                    </div>
                </div>
                <div class="col-6">
                    <div class="d-flex mt-1" t-if="o.date">
                        <h6 class="col-3 fw-bold">Date:</h6>
                        <h6 t-field="o.date">07/07/2023 10:00:00</h6>
                    </div>
                    <div class="d-flex mt-1" t-if="o.date_start">
                        <h6 class="col-3 fw-bold">Period:</h6>
                        <h6>
                            <span t-field="o.date_start">07/07/2023 10:00:00</span> <span class="fw-bold">To</span> <span t-field="o.date_end">07/08/2023 10:00:00</span>
                        </h6>
                    </div>
                    <div class="d-flex mt-1" t-if="o.location">
                        <h6 class="col-3 fw-bold">Location:</h6>
                        <h6 t-field="o.location">Brussels</h6>
                    </div>
                    <div class="d-flex mt-1" t-if="o.partner_id">
                        <h6 class="col-3 fw-bold">Contact:</h6>
                        <h6 t-field="o.partner_id">Mitchell Admin</h6>
                    </div>
                    <div class="d-flex mt-1" t-if="o.amount">
                        <h6 class="col-3 fw-bold">Amount:</h6>
                        <h6 t-field="o.amount">1200</h6>
                    </div>
                </div>
            </div>
            <div class="page mt-4" t-if="o.product_line_ids">
                <div class="oe_structure"/>
                <table class="table table-sm mt-4">
                    <thead class="o_black_border">
                        <tr>
                            <th name="th_description" class="text-start fw-bold">Product Description</th>
                            <th name="th_expected_date" class="text-center fw-bold">Quantity</th>
                            <th name="th_uom" class="text-center fw-bold">Unit</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr t-foreach="o.product_line_ids" t-as="product_line">
                            <td><span t-field="product_line.product_id">Test Product</span></td>
                            <td class="text-center"><span t-field="product_line.quantity">2</span></td>
                            <td class="text-center"><span t-field="product_line.product_uom_id">Units</span></td>
                        </tr>
                    </tbody>
                </table>
                <div class="oe_structure"/>
            </div>
            <div t-if="o.reason" class="mt-4">
                <h6 class="d-flex">
                    <span class="col-2 fw-bold">Description:</span>
                    <span t-field="o.reason">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
                </h6>
            </div>
            <div class="row mt-4" t-if="o.reference">
                <div class="d-flex">
                    <h6 class="col-2 fw-bold">Reference:</h6>
                    <h6 t-field="o.reference">Test Reference</h6>
                </div>
            </div>
            <div class="row mt-4" t-if="o.attachment_ids.ids">
                <div class="d-flex">
                    <h6 class="col-2 fw-bold">Documents:</h6>
                    <h6 t-foreach="o.attachment_ids" t-as="attachment" t-out="attachment.name">Test Document</h6>
                </div>
            </div>
        </t>
    </template>

    <template id="report_approval_request">
        <t t-call="web.html_container">
            <t t-foreach="docs" t-as="o">
                <t t-call="approvals.report_aprroval_request_document" t-lang="o.partner_id.lang"/>
            </t>
        </t>
    </template>
</odoo>
```

## File: views/approval_request_views.xml
```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>

<!--Request-->

    <record id="approval_request_action" model="ir.actions.act_window">
        <field name="name">My Requests</field>
        <field name="res_model">approval.request</field>
        <field name="view_mode">kanban,list,form</field>
        <field name="domain">[('request_owner_id','=',uid)]</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                No Approvals Requests
            </p>
            <p>
                Let's go to the <a type="action" class="text-primary" name="%(approvals.approval_category_action_new_request)d">new request</a> menu
            </p>
        </field>
    </record>

    <record id="approval_request_action_to_review" model="ir.actions.act_window">
        <field name="name">Approvals to Review</field>
        <field name="res_model">approval.request</field>
        <field name="view_mode">list,form,kanban</field>
        <field name="domain">['&amp;',('approver_ids.user_id','=',uid),('request_status','=','pending')]</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                No new approvals to review
            </p>
        </field>
    </record>

    <record id="approval_request_action_all" model="ir.actions.act_window">
        <field name="name">All Approvals</field>
        <field name="res_model">approval.request</field>
        <field name="view_mode">list,form,kanban</field>
        <field name="help" type="html">
            <p class="o_view_nocontent_smiling_face">
                No Approvals
            </p>
            <p>
                Let's go to the <a type="action" class="text-primary" name="%(approvals.approval_category_action_new_request)d">new request</a> menu
            </p>
        </field>
    </record>

    <record id="approval_request_view_tree" model="ir.ui.view">
        <field name="name">approval.request.view.list</field>
        <field name="model">approval.request</field>
        <field name="priority">10</field>
        <field name="arch" type="xml">
            <list sample="1" decoration-info="request_status == 'new'">
                <field name="name"/>
                <field name="request_owner_id" widget="many2one_avatar_user"/>
                <field name="category_id"/>
                <field name="date_start" string="Request Start"  optional="show"/>
                <field name="date_end" string="Request To" optional="show"/>
                <field name="date_confirmed" string="Confirm Date" optional="hide"/>
                <field name="location" string="Location" optional="hide"/>
                <field name="activity_ids" widget="list_activity" optional="hide"/>
                <field name="user_ids" string="Approvers" widget="many2many_avatar_user" optional="hide"/>
                <field name="request_status" decoration-info="request_status == 'new'" decoration-warning="request_status == 'pending'" decoration-success="request_status == 'approved'" decoration-danger="request_status == 'refused'" widget="badge"/>
                <field name="approval_properties"/>
                <field name="company_id" readonly="True" optional="hide" groups="base.group_multi_company"/>
            </list>
        </field>
    </record>

    <record id="approval_search_view_search" model="ir.ui.view">
        <field name="name">approval.request.search</field>
        <field name="model">approval.request</field>
        <field name="priority">20</field>
        <field name="arch" type="xml">
            <search>
                <field name="name"/>
                <filter string="My Request" name="filter_my_request" domain="[('request_owner_id', '=', uid)]"/>
                <filter string="My Approvals to Review" name="filter_approvals_to_review"
                    domain="[('approver_ids.user_id', '=', uid), ('request_status', '=', 'pending')]"/>
                <separator/>
                <filter string="Approved" name="filter_approved_requests" domain="[('request_status', '=', 'approved')]"/>
                <filter string="Refused" name="filter_refused_requests" domain="[('request_status', '=', 'refused')]"/>
                <separator/>
                <filter string="Canceled" name="filter_canceled_requests" domain="[('request_status', '=', 'cancel')]"/>
                <separator/>
                <filter string="Archived" name="filter_archived_requests" domain="[('active', '=', False)]"/>
                <filter invisible="1" string="Late Activities" name="activities_overdue"
                    domain="[('my_activity_date_deadline', '&lt;', 'today')]"/>
                <filter invisible="1" string="Today Activities" name="activities_today"
                    domain="[('my_activity_date_deadline', '=', 'today')]"/>
                <filter invisible="1" string="Future Activities" name="activities_upcoming_all"
                    domain="[('my_activity_date_deadline', '&gt;', 'today')]"/>
                <group>
                    <filter string="Request Owner" name="groupby_request_owner"
                        context="{'group_by': 'request_owner_id'}"/>
                    <filter string="Category" name="groupby_category_id"
                        context="{'group_by': 'category_id'}"/>
                    <filter string="Request Status" name="groupby_request_status"
                        context="{'group_by': 'request_status'}"/>
                </group>
            </search>
        </field>
    </record>

    <record id="approval_request_view_form" model="ir.ui.view">
        <field name="name">approval.request.view.form</field>
        <field name="model">approval.request</field>
        <field name="priority">10</field>
        <field name="arch" type="xml">
            <form string="Request">
                <header>
                    <field name="user_status" invisible="1"/>
                    <field name="has_access_to_request" invisible="1"/>
                    <widget name="attach_document" string="Attach Document" action="message_post" highlight="1" invisible="(attachment_number &gt;= 1 and request_owner_id == uid) or request_owner_id != uid"/>
                    <button name="action_confirm" string="Submit" type="object" invisible="attachment_number &lt; 1 or not approver_ids or request_status != 'new'" class="btn-primary" data-hotkey="q"/>
                    <button name="action_confirm" string="Submit" type="object" invisible="attachment_number &gt;= 1 or not approver_ids or request_status != 'new'" data-hotkey="q"/>
                    <button name="action_approve" string="Approve" type="object" invisible="(attachment_number &lt; 1 and request_owner_id == uid) or request_status in ['approved', 'refused', 'cancel'] or user_status != 'pending'" class="btn-primary" data-hotkey="v"/>
                    <button name="action_approve" string="Approve" type="object" invisible="attachment_number &gt;= 1 or request_owner_id != uid or request_status in ['approved', 'refused', 'cancel'] or user_status != 'pending'" class="btn-primary" data-hotkey="v"/>
                    <button name="action_refuse" string="Refuse" type="object" invisible="request_status in ['approved', 'refused', 'cancel'] or user_status != 'pending'" data-hotkey="z"/>
                    <button name="action_withdraw" string="Withdraw" type="object" invisible="request_status == 'new' or user_status in ['waiting', 'pending', 'cancel'] or not user_status" data-hotkey="y"/>
                    <button name="action_draft" string="Back To Draft" type="object" invisible="request_status != 'cancel' or not user_status and not has_access_to_request" data-hotkey="w"/>
                    <button name="action_cancel" string="Cancel" type="object" invisible="request_status in ['new', 'cancel'] or request_owner_id != uid" data-hotkey="x"/>
                    <widget name="attach_document" string="Attach Document" action="message_post" invisible="(attachment_number &lt; 1 and request_owner_id == uid)"/>
                    <button string="Print" invisible="request_status != 'approved' or approval_type !='purchase'" type="action" name="%(action_report_approval_request)d"/>
                    <field name="request_status" widget="statusbar" statusbar_visible="new,pending,approved,refused" />
                </header>
                <sheet>
                    <field name="active" invisible="1"/>
                    <field name="has_date" invisible="1"/>
                    <field name="has_period" invisible="1"/>
                    <field name="has_quantity" invisible="1"/>
                    <field name="has_amount" invisible="1"/>
                    <field name="has_reference" invisible="1"/>
                    <field name="has_partner" invisible="1"/>
                    <field name="has_payment_method" invisible="1"/>
                    <field name="has_location" invisible="1"/>
                    <field name="has_product" invisible="1"/>
                    <field name="requirer_document" invisible="1"/>
                    <field name="approval_minimum" invisible="1"/>
                    <field name="approval_type" invisible="1"/>
                    <field name="change_request_owner" invisible="1"/>
                    <div class="o_not_full oe_button_box" name="button_box">
                        <button name="action_get_attachment_view"
                            class="oe_stat_button"
                            icon="fa-book"
                            type="object"
                            invisible="attachment_number == 0">
                            <field name="attachment_number" widget="statinfo" string="Documents" options="{'reload_on_button': true}"/>
                        </button>
                    </div>
                    <div class="oe_avatar">
                        <field name="category_image" widget="image" options="{'preview_image': 'category_image', 'size': [80, 80]}" class="bg-view" />
                    </div>
                    <widget name="web_ribbon" title="Archived" bg_color="text-bg-danger" invisible="active"/>
                    <div class="oe_title">
                        <label for="name"/>
                        <h1>
                            <field name="automated_sequence" invisible="1"/>
                            <field name="name" placeholder="E.g: Expenses Paris business trip"
                                required="not automated_sequence"
                                readonly="automated_sequence"/>
                        </h1>
                    </div>
                    <group>
                        <group name="request_main">
                            <field name="request_owner_id" readonly="not change_request_owner or request_status != 'new'" widget="many2one_avatar_user"/>
                            <field name="category_id" readonly="request_status != 'new'" force_save="1"/>
                            <field name="date_confirmed" groups="base.group_no_one" readonly="1"/>
                            <label for="date" string="Date" invisible="has_date == 'no'"/>
                            <div invisible="has_date == 'no'">
                                <div>
                                    <field name="date" class="oe_inline" readonly="request_status != 'new'" required="has_date == 'required'"/>
                                </div>
                            </div>
                            <label for="date_start" string="Period" invisible="has_period == 'no'"/>
                            <div invisible="has_period == 'no'">
                                <div>
                                    <label for="date_start" class="col-lg-2" string="From:"/>
                                    <field name="date_start" class="oe_inline" readonly="request_status != 'new'" required="has_period == 'required'"/>
                                </div>
                                <div>
                                    <label for="date_end" class="col-lg-2" string="to:"/>
                                    <field name="date_end" class="oe_inline" readonly="request_status != 'new'" required="has_period == 'required'"/>
                                </div>
                            </div>
                            <field name="location" invisible="has_location == 'no'" readonly="request_status != 'new'" required="has_location == 'required'" placeholder="e.g. Brussels" />
                            <field name="partner_id" invisible="has_partner == 'no'" readonly="request_status != 'new'" required="has_partner == 'required'" context="{'category_id': ''}"/>
                            <field name="company_id" groups="base.group_multi_company"/>
                        </group>
                        <group name="request_details">
                            <field name="quantity" invisible="has_quantity == 'no' or has_product != 'no'" readonly="request_status != 'new'" required="has_quantity == 'required' and has_product == 'no'"/>
                            <field name="amount" invisible="has_amount == 'no'" readonly="request_status != 'new'" required="has_amount == 'required'"/>
                            <field name="reference" invisible="has_reference == 'no'" required="has_reference == 'required'"/>
                            <field name="company_id" invisible="1"/>
                        </group>
                        <field name="approval_properties" columns="2"/>
                    </group>
                    <notebook>
                        <page string="Products" name="products"
                            invisible="has_product == 'no'">
                            <field name="product_line_ids"
                                context="{'list_view_ref': 'approvals.approval_product_line_view_tree', 'kanban_view_ref': 'approvals.approval_product_kanban_mobile_view'}"
                                readonly="request_status != 'new'"/>
                        </page>
                        <page string="Description" name="description">
                            <field name="reason" readonly="request_status != 'new'"/>
                        </page>
                        <page string="Approver(s)" name="approvers">
                            <field name="approver_ids" mode="list,kanban" readonly="request_status != 'new' or change_request_owner == False">
                                <list editable="bottom" decoration-success="status=='approved'" decoration-warning="status in ['pending', 'waiting']" decoration-danger="status=='refused'" no_open="1">
                                    <field name="existing_request_user_ids" column_invisible="True"/>
                                    <field name="sequence" column_invisible="True"/>
                                    <field name="can_edit" column_invisible="True"/>
                                    <field name="can_edit_user_id" column_invisible="True"/>
                                    <field name="user_id" string="Approver" widget="many2one_avatar_user" readonly="not can_edit_user_id or status != 'new'" force_save="1" />
                                    <field name="required" readonly="not can_edit" force_save="1"/>
                                    <field name="status"/>
                                    <field name="company_id" column_invisible="True"/>
                                </list>
                                <kanban class="o_kanban_mobile">
                                    <templates>
                                        <t t-name="card" class="flex-row">
                                            <field name="user_id"/>
                                            <t t-if="record.status.raw_value">
                                                <t t-set="classname" t-value="{'approved': 'text-bg-success', 'pending': 'text-bg-warning', 'refused': 'text-bg-danger'}[record.status.raw_value] || 'text-bg-light'"/>
                                                <span t-attf-class="ms-auto rounded-pill {{ classname }}">
                                                    <field name="status"/>
                                                </span>
                                            </t>
                                        </t>
                                    </templates>
                                </kanban>
                                <form>
                                    <group>
                                        <field name="company_id" invisible="1"/>
                                        <field name="existing_request_user_ids" invisible="1"/>
                                        <field name="user_id"/>
                                    </group>
                                </form>
                            </field>
                        </page>
                    </notebook>
                </sheet>
                <div class="o_attachment_preview"/>
                <chatter/>
            </form>
        </field>
    </record>

    <record id="approval_request_view_kanban" model="ir.ui.view">
        <field name="name">approval.request.view.kanban</field>
        <field name="model">approval.request</field>
        <field name="arch" type="xml">
            <kanban create="false" class="o_modules_kanban" default_group_by="request_status" default_order="create_date desc" 
            group_create="false" group_edit="false" group_delete="false" sample="1">
                <field name="request_status"/>
                <field name="user_status"/>
                <field name="date_start"/>
                <field name="date_end"/>
                <templates>
                    <t t-name="card">
                        <div class="row g-2">
                            <div class="col-auto">
                                <field name="category_image" widget="image" options="{'preview_image': 'category_image', 'size': [64, 64]}"/>
                            </div>
                            <div class="col">
                                <field name="request_status"
                                       widget="badge"
                                       class="float-end"
                                       decoration-info="request_status == 'new'"
                                       decoration-warning="request_status == 'pending'"
                                       decoration-success="request_status == 'approved'"
                                       decoration-danger="request_status == 'refused'"/>
                                <field name="name" class="fw-bolder fs-3 pe-5 d-block text-wrap"/>
                                <field name="request_owner_id" widget="many2one_avatar_user" options="{'display_avatar_name': True}" class="o_approval_kanban_avatar fw-bold my-1"/>
                                <div class="text-muted">
                                    <t t-if="record.date_start.raw_value" t-out="luxon.DateTime.fromISO(record.date_start.raw_value).toLocaleString({ month: 'short', day: 'numeric', year: 'numeric'})"/>
                                    <t t-if="record.date_end.raw_value and record.date_start.raw_value != record.date_end.raw_value">
                                        <span class="mx-1">-</span>
                                        <t t-out="luxon.DateTime.fromISO(record.date_end.raw_value).toLocaleString({ month: 'short', day: 'numeric', year: 'numeric'})"/>
                                    </t>
                                </div>
                            </div>
                        </div>
                        <footer class="o_kanban_footer">
                            <div class="d-flex align-items-center w-100">
                                <div class="d-flex gap-2 ms-auto">
                                    <button t-if="record.user_status.raw_value == 'pending'" name="action_approve" type="object" class="btn btn-sm py-0">
                                        <i class="fa fa-check text-success me-1"/>Approve
                                    </button>
                                    <button t-if="record.user_status.raw_value == 'pending'" name="action_refuse" type="object" class="btn btn-sm py-0">
                                        <i class="fa fa-times text-danger me-1"/>Refuse
                                    </button>
                                </div>
                                <field name="activity_ids" widget="kanban_activity"/>
                            </div>
                        </footer>
                    </t>
                </templates>
            </kanban>
        </field>
    </record>

    <record id="model_approval_request_approve_admin" model="ir.actions.server">
        <field name="name">Force Approval</field>
        <field name="model_id" ref="approvals.model_approval_request"/>
        <field name="binding_model_id" ref="approvals.model_approval_request"/>
        <field name="group_ids" eval="[(4, ref('approvals.group_approval_user'))]"/>
        <field name="binding_view_types">form,list</field>
        <field name="state">code</field>
        <field name="code">
if records:
    records._action_force_approval()
        </field>
    </record>

<!--MenuItem-->

    <menuitem
        id="approvals_menu_root"
        name="Approvals"
        web_icon="approvals,static/description/icon.png"
        action="approval_category_action_new_request"
        sequence="255"/>

    <menuitem
        id="approvals_category_menu_new"
        parent="approvals_menu_root"
        name="Dashboard"
        action="approval_category_action_new_request"
        sequence="1"/>

    <menuitem
        id="approvals_approval_menu"
        parent="approvals_menu_root"
        name="My Approvals"
        sequence="10"/>

    <menuitem
        id="approvals_request_menu_my"
        parent="approvals_approval_menu"
        name="My Requests"
        action="approval_request_action"
        sequence="20"/>

    <menuitem
        id="approvals_menu_manager"
        parent="approvals_menu_root"
        name="Manager"
        sequence="20"/>

    <menuitem
        id="approvals_approval_menu_to_review"
        parent="approvals_menu_manager"
        name="Approvals to Review"
        action="approval_request_action_to_review"
        sequence="10"/>

    <menuitem
        id="approvals_approval_menu_all"
        parent="approvals_menu_manager"
        name="All Approvals"
        action="approval_request_action_all"
        sequence="20"/>

    <menuitem
        id="approvals_menu_config"
        parent="approvals_menu_root"
        name="Configuration"
        groups="group_approval_manager"
        sequence="40"/>

    <menuitem
        id="approvals_category_menu_config"
        parent="approvals_menu_config"
        name="Approval Categories"
        action="approval_category_action"
        groups="group_approval_manager"
        sequence="10"/>

    <menuitem
        id="approvals_menu_product"
        parent="approvals_menu_config"
        name="Products"
        sequence="30"/>

    <menuitem
        id="approvals_menu_product_template"
        parent="approvals_menu_product"
        name="Products"
        action="product_template_action"
        sequence="10"/>

    <menuitem
        id="approvals_menu_product_variant"
        parent="approvals_menu_product"
        name="Product Variants"
        action="product_product_action"
        groups="product.group_product_variant"
        sequence="20"/>
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
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Approvals',
    'version': '1.1',
    'category': 'Human Resources/Approvals',
    'sequence': 190,
    'summary': 'Create and validate approvals requests',
    'description': """
This module manages approvals workflow
======================================

This module manages approval requests like business trips,
out of office, overtime, borrow items, general approvals,
procurements, contract approval, etc.

According to the approval type configuration, a request
creates next activities for the related approvers.
    """,
    'depends': ['mail', 'hr', 'product'],
    'data': [
        'security/approval_security.xml',
        'security/ir.model.access.csv',

        'data/approval_category_data.xml',
        'data/mail_activity_type_data.xml',
        'data/mail_message_subtype_data.xml',

        'views/approval_category_views.xml',
        'views/approval_category_approver_views.xml',
        'views/approval_product_line_views.xml',
        'views/approval_products_views.xml',
        'views/approval_request_template.xml',
        'report/approval_request_report.xml',
        'views/approval_request_views.xml',
    ],
    'demo':[
        'data/approval_demo.xml',
    ],
    'application': True,
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'approvals/static/src/common/**',
            'approvals/static/src/web/**',
            'approvals/static/src/views/**',
            'approvals/static/src/scss/**',
        ],
        'mail.assets_public': [
            'approvals/static/src/common/**',
         ],
        'web.assets_tests': [
            'approvals/static/tests/tours/**/*',
        ],
        'web.assets_unit_tests': [
            'approvals/static/tests/**/*',
            ('remove', 'approvals/static/tests/tours/**/*'),
        ],
    },
    'author': 'Odoo S.A.',
    'license': 'OEEL-1',
}
```
