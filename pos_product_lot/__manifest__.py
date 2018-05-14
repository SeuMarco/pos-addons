{
    'name': 'Product lot in POS',
    'version': '1.0.2',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    'website': 'https://twitter.com/yelizariev',
    'images': ['images/screenshot.png'],
    'depends': ['product_lot', 'pos_product_available'],
    'data': [
        'data.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': False,
    'auto_install': False,
}
