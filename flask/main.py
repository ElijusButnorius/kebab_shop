from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'kebab_shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #kas pagerintu veikima ir sumazintu naudojama atminti.  Isjungia sql alchemy sekti objektu modifikacija
db = SQLAlchemy(app) # sos kodas sukuria SQLAlchemy objekta.

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    sudetis = db.Column(db.String(200), nullable=False)
    aktyvi = db.Column(db.Boolean, default=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products_view():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/orders')
def orders_view():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        product_id = int(request.form['product_id'])
        new_order = Order(product_id=product_id)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('orders_view'))
    products = Product.query.filter_by(aktyvi=True).all()
    return render_template('add_order.html', products=products)

@app.route('/delete_order/<int:order_id>')
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('orders_view'))

if __name__ == '__main__':
    app.run(debug=True)
