from app import app 
from flask import render_template


# MAIN APPLICATION ROUTES
@app.route('/')
def home():
    return render_template('main/home.html')

@app.route('/contact')
def contact():
    return 'Contact Page'

@app.route('/profile')
def profile():
    return render_template('main/profile.html')

# USER ROUTES
@app.route('/users')
def users_list():
    return 'Users Page'

@app.route('/users/<id>')
def user_single():
    return 'User Single Page'


# SHOP ROUTES
@app.route('/shop')
def shop_list():
    return 'Shop Page'

@app.route('/shop/<id>')
def shop_single():
    return 'Shop Single Page'

@app.route('/shop/cart')
def shop_cart():
    return 'Shop Cart Page'

@app.route('/shop/checkout')
def shop_checkout():
    return 'Shop Checkout Page'




