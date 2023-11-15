```python
from odoo import models, fields

class Review(models.Model):
    _name = 'ecommerce_theme_v1.review'
    _description = 'Review'

    id = fields.Integer(string='ID', required=True)
    product_id = fields.Many2one('ecommerce_theme_v1.product', string='Product', required=True)
    user_id = fields.Many2one('ecommerce_theme_v1.user', string='User', required=True)
    content = fields.Text(string='Review Content', required=True)
```