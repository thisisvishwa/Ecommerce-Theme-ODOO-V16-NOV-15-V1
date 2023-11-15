{
    'name': 'ecommerce_theme_v1',
    'version': '1.0',
    'category': 'Theme/Ecommerce',
    'summary': 'Ecommerce theme for selling gaming PCs, laptops, PC components, gaming consoles, and similar products',
    'sequence': 1,
    'description': """
    This is an ecommerce theme developed for Odoo v16 Community Edition. 
    It includes features like product catalog, shopping cart, checkout process, search functionality, user account management, and customer reviews.
    """,
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'depends': ['website_sale', 'website_theme_install'],
    'data': [
        'views/product_template.xml',
        'views/user_template.xml',
        'views/review_template.xml',
        'views/cart_template.xml',
        'views/checkout_template.xml',
        'views/search_template.xml',
        'data/product_data.xml',
        'data/user_data.xml',
        'data/review_data.xml',
        'data/cart_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'qweb': [],
}