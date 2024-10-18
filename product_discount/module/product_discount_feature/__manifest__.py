# -*- coding: utf-8 -*-
{
    'name': 'Product Discount Feature',
    'summary': 'Product Discount Feature',
    'description': """
    """,
    'sequence': 1,
    'license':"LGPL-3",
    'author': '',
    'sequence': 1,
    'version': '16.0.0',
    'depends':['website_sale','sale','account','stock','delivery'],

    'data': [
        'static/src/templates/templates.xml',
        'views/product_template_view.xml',
        'views/report_invoice.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
