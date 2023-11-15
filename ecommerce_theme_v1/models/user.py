```python
from odoo import models, fields

class User(models.Model):
    _name = 'ecommerce_theme_v1.user'
    _description = 'User Model for eCommerce Theme'

    id = fields.Char(string='ID', required=True, index=True)
    username = fields.Char(string='Username', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password', required=True)
    preferred_payment_method = fields.Selection([
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
    ], string='Preferred Payment Method')
    order_history = fields.One2many('ecommerce_theme_v1.order', 'user_id', string='Order History')

    def create_user(self, username, email, password):
        self.create({
            'username': username,
            'email': email,
            'password': password,
        })

    def login(self, username, password):
        user = self.search([('username', '=', username), ('password', '=', password)])
        if user:
            return True
        return False

    def logout(self):
        # Logout logic goes here
        pass
```