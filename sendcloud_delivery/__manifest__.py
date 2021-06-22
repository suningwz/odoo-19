# -*- coding: utf-8 -*-
{
    'name': 'SendCloud Odoo Shipping Integration',
    'version': '14.0',
    'category': 'Warehouse',
    'summary': 'Integrate & Manage your SendCloud Shipping Operations from Odoo',

    'depends': ['base_shipping_partner'],

    'data': [
        'views/assets.xml',
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/shipping_partner_view.xml',
        'views/delivery_carrier_view.xml',
        'views/sendcloud_service_view.xml',
        'views/sendcloud_integration_view.xml',
        'views/stock_picking_view.xml',
    ],

    'images': ['static/description/sendcloud_odoo.png'],

    'author': 'Teqstars',
    'website': 'https://teqstars.com',
    'support': 'support@teqstars.com',
    'maintainer': 'Teqstars',
    "description": """
        - Send Cloud Service point picker
        - SendCloud Service point picker
        - Send Cloud
        - Manage your Send Cloud operation from Odoo
        - Integration Send Cloud
        - Connector Send Cloud
        - Send Cloud Connector
        - Odoo Send Cloud Connector
        - Send Cloud integration
        - Send Cloud odoo connector
        - Send Cloud odoo integration
        - Send Cloud shipping integration
        - Send Cloud integration with Odoo
        - odoo Send Cloud integration
        - odoo integration with Send Cloud
        - all in one shipping software for e-commerce
        - Manage your SendCloud operation from Odoo
        - Integration SendCloud
        - Connector SendCloud
        - SendCloud Connector
        - Odoo SendCloud Connector
        - SendCloud integration
        - SendCloud odoo connector
        - SendCloud odoo integration
        - SendCloud shipping integration
        - SendCloud integration with Odoo
        - odoo integration apps
        - odoo SendCloud integration
        - odoo integration with SendCloud
        - shipping integation
        - shipping provider integration
        - shipper integration
        """,

    'qweb': ['static/src/xml/*.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'price': '99.99',
    'currency': 'EUR',
}
