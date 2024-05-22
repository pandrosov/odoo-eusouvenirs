{
    'name': 'Custom Sale Report Module',
    'version': '1.0',
    'summary': 'Custom sale report similar to Order/Quotation without prices',
    'description': 'Generates a PDF report similar to Order/Quotation but without prices.',
    'author': 'Your Name',
    'depends': ['base', 'sale'],
    'data': [
        'views/reports_view.xml',
        'report/custom_sale_report_template.xml',
    ],
    'installable': True,
    'application': False,
}
