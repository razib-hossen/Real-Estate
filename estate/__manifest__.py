{
    'name': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Rajib Mahmud',
    'category': 'Services',
    'description': """
    The Real Estate Advertisement module.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',

    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'icon': '/estate/static/description/icon1.png',
    'license': 'LGPL-3',
}
