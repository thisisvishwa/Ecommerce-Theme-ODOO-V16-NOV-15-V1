```python
from odoo import models, fields

class Cart(models.Model):
    _name = 'ecommerce_theme_v1.cart'
    _description = 'Shopping Cart'

    user_id = fields.Many2one('ecommerce_theme_v1.user', string='User')
    product_id = fields.Many2one('ecommerce_theme_v1.product', string='Product')
    quantity = fields.Integer(string='Quantity', default=1)

    def add_to_cart(self, product_id):
        self.ensure_one()
        self.write({
            'product_id': product_id,
            'quantity': self.quantity + 1
        })

    def remove_from_cart(self, product_id):
        self.ensure_one()
        if self.product_id.id == product_id and self.quantity > 0:
            self.write({
                'quantity': self.quantity - 1
            })

    def checkout(self):
        self.ensure_one()
        # Implement checkout logic here
        pass
```