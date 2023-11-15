```python
from odoo import http
from odoo.http import request

class EcommerceController(http.Controller):

    @http.route('/shop', type='http', auth='public', website=True)
    def shop(self, **kwargs):
        products = request.env['product.product'].search([])
        return request.render('ecommerce_theme_v1.product_template', {'products': products})

    @http.route('/cart', type='http', auth='user', website=True)
    def cart(self, **kwargs):
        cart = request.env['sale.order'].search([('state', '=', 'draft'), ('user_id', '=', request.uid)], limit=1)
        return request.render('ecommerce_theme_v1.cart_template', {'cart': cart})

    @http.route('/checkout', type='http', auth='user', website=True)
    def checkout(self, **kwargs):
        cart = request.env['sale.order'].search([('state', '=', 'draft'), ('user_id', '=', request.uid)], limit=1)
        return request.render('ecommerce_theme_v1.checkout_template', {'cart': cart})

    @http.route('/search', type='http', auth='public', website=True)
    def search(self, q=None, **kwargs):
        domain = [('name', 'ilike', q)] if q else []
        products = request.env['product.product'].search(domain)
        return request.render('ecommerce_theme_v1.search_template', {'products': products})

    @http.route('/account', type='http', auth='user', website=True)
    def account(self, **kwargs):
        user = request.env['res.users'].browse(request.uid)
        return request.render('ecommerce_theme_v1.user_template', {'user': user})

    @http.route('/review', type='http', auth='user', website=True, methods=['POST'])
    def review(self, product_id, content, **kwargs):
        request.env['product.review'].create({
            'product_id': product_id,
            'user_id': request.uid,
            'content': content
        })
        return request.redirect('/shop')
```