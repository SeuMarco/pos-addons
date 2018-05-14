{
    'name': "POS debranding",
    'version': '1.0.0',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'LGPL-3',
    'category': 'Debranding',
    "support": "apps@it-projects.info",
    'website': 'https://twitter.com/yelizariev',
    'depends': ['point_of_sale'],
    'data': [
        'views.xml',
    ],
    'qweb': [
        'static/src/xml/pos_debranding.xml',
    ],
    'installable': True,
}
