```python
from odoo import models, fields

class Product(models.Model):
    _name = 'ecommerce_theme_v1.product'
    _description = 'Product Model for eCommerce Theme'

    id = fields.Char(string='ID', required=True, index=True)
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    image = fields.Binary(string='Image')
    product_type = fields.Selection([
        ('gaming_pc', 'Gaming PC'),
        ('laptop', 'Laptop'),
        ('pc_component', 'PC Component'),
        ('gaming_console', 'Gaming Console'),
    ], string='Product Type', required=True)
```