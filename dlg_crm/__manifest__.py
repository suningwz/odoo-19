# -*- coding: utf-8 -*-
{
    'name': "dlg_crm",

    'summary': """
        Módulo CRM para la gestión de oportunidades""",

    'description': """
        Módulo CRM para la gestión de oportunidades...
    """,

    'author': "DLG219",
    'website': "http://www.delegalog.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/phase.xml',
        'views/opportunity.xml',
        'views/action.xml',
        'views/templates.xml',
        'reports/phase.xml',
        'reports/opportunity.xml',
        'reports/action.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
