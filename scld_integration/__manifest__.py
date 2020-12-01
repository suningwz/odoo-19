# -*- coding: utf-8 -*-
{
    'name': "scld_integration",

    'summary': """
        SendCloud Odoo Integration""",

    'description': """
        SendCloud Odoo Integration...
    """,

    'author': "delegalog",
    'website': "http://www.delegalog.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/parcel.xml'
    ],

    'application': True,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
