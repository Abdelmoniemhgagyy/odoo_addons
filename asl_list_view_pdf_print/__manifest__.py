{
    'name': 'List View PDF Print',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Export any list view to a professional PDF report dynamically.',
    'description': """
List View PDF Print
===================

Adds a generic "Print PDF" action to every list view in Odoo.

Features
--------
* Works on all list views - Sales, Invoices, Contacts, custom models and more
* Dynamic column detection - prints exactly the columns you see
* Respects the current search filters and domain
* Print all filtered records or only the selected rows
* Automatic grand totals for numeric columns
* Supports Odoo's grouping and clean, professional styling
    """,
    'author': 'Abdulrahman Elassal',
    'website': 'https://github.com/AbdulrahmanElassal',
    'support': 'abdulrahmanelassal47@gmail.com',
    'depends': ['web'],
    'data': [
        'reports/report_actions.xml',
        'reports/report_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'asl_list_view_pdf_print/static/src/views/list/**/*',
        ],
    },
    'images': [
        'static/description/cover.png',
        'static/description/print_all_menu.png',
        'static/description/print_selected_menu.png',
        'static/description/all_records_totals.png',
        'static/description/selected_records_totals.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
