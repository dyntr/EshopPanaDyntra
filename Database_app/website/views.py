"""
Flask Web Application - E-shop

Tento skript implementuje webovou aplikaci pro e-shop pomocí Flask frameworku. Obsahuje různé pohledy a funkce pro správu produktů, zákazníků, objednávek a transakcí.

Třídy a funkce zahrnují:

1. @views.route('/home') - Přesměrování na úvodní stránku.
2. @views.route('/login') - Přihlášení uživatele.
3. @views.route('/register') - Registrace nového uživatele.
4. @views.route('/') - Zobrazení seznamu produktů.
5. @views.route('/products') - Zobrazení seznamu produktů.
6. @views.route('/products_by_type/<string:type>') - Zobrazení produktů podle typu.
7. @views.route('/search') - Vyhledávání produktů.
8. @views.route('/add_to_cart') - Přidání produktu do košíku.
9. @views.route('/cart') - Zobrazení obsahu košíku.
10. @views.route('/buy') - Vytvoření objednávky.
11. @views.route('/cart/remove/<int:id>') - Odstranění produktu z košíku.
12. @views.route('/order_history') - Zobrazení historie objednávek.
"""

from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from src.db_connect import DbConnection
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/home')
def home():
    # Přesměrování na úvodní stránku
    return redirect(url_for('views.index'))

@views.route('/login')
def login():
    # Zobrazení přihlašovací stránky
    return render_template('auth.php')

@views.route('/register')
def register():
    # Zobrazení registrační stránky
    return render_template('auth.php')

@views.route('/', methods=['GET', 'POST'])
def index():
    # Zobrazení seznamu produktů
    return product_list()

@views.route('/products', methods=['GET', 'POST'])
def products():
    # Zobrazení seznamu produktů
    return product_list()

@views.route('/products_by_type/<string:type>', methods=['GET', 'POST'])
def products_by_type(type):
    # Zobrazení produktů podle typu
    return product_list(type)

def product_list(type=None):
    # Funkce pro zobrazení seznamu produktů
    db_conn = DbConnection.get_instance()
    cursor = db_conn.connection.cursor(dictionary=True)

    query = 'SELECT * FROM product WHERE 1=1'
    params = []

    if type:
        query += ' AND Type=%s'
        params.append(type)

    if request.method == 'POST':
        min_price = request.form.get('min-price')
        max_price = request.form.get('max-price')
        price_order = request.form.get('price')

        if min_price:
            query += ' AND Price >= %s'
            params.append(min_price)
        if max_price:
            query += ' AND Price <= %s'
            params.append(max_price)
        if price_order:
            if price_order == 'asc':
                query += ' ORDER BY Price ASC'
            elif price_order == 'desc':
                query += ' ORDER BY Price DESC'

    cursor.execute(query, params)
    products = cursor.fetchall()

    cursor.execute('SELECT DISTINCT Type FROM product')
    types = [row['Type'] for row in cursor.fetchall()]

    username = session.get('username')
    return render_template('base.php', products=products, types=types, username=username, current_type=type)

@views.route('/search')
def search():
    # Funkce pro vyhledávání produktů
    db_conn = DbConnection.get_instance()
    cursor = db_conn.connection.cursor(dictionary=True)

    search_term = request.args.get('q')
    sql = "SELECT * FROM product WHERE Name LIKE %s"
    search_term = f"{search_term}%"
    cursor.execute(sql, (search_term,))
    products = cursor.fetchall()

    return render_template('search.php', products=products, search_term=search_term)

@views.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Funkce pro přidání produktu do košíku
    product_id = request.form.get('product_id')

    if product_id:
        db_conn = DbConnection.get_instance()
        cursor = db_conn.connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM product WHERE ID=%s', (product_id,))
        product = cursor.fetchone()
        if product:
            cart = session.get('cart', [])
            if isinstance(cart, dict):
                cart = list(cart.keys())  # Convert the cart from a dictionary to a list of product IDs
            cart.append(int(product_id))
            session['cart'] = cart
            return redirect(request.referrer)

    flash('Product not found', 'error')
    return redirect(url_for('views.index'))

@views.route('/cart')
def cart():
    # Funkce pro zobrazení obsahu košíku
    db_conn = DbConnection.get_instance()
    cursor = db_conn.connection.cursor(dictionary=True)

    product_ids = session.get('cart', [])
    quantities = {}
    total_price = 0
    products = []

    for product_id in product_ids:
        quantities[product_id] = quantities.get(product_id, 0) + 1

    for product_id, quantity in quantities.items():
        cursor.execute('SELECT * FROM product WHERE id=%s', (product_id,))
        product = cursor.fetchone()
        if product:
            product['Quantity'] = quantity
            product['Total_price'] = product['Price'] * quantity
            total_price += product['Total_price']
            products.append(product)

    return render_template('cart.php', products=products, total_price=total_price)

@views.route('/buy', methods=['POST'])
def buy():
    # Funkce pro vytvoření objednávky
    db_conn = DbConnection.get_instance()
    cursor = db_conn.connection.cursor(dictionary=True)
    if 'username' not in session:
        flash('You need to log in to place an order!', 'error')
        return redirect(url_for('views.login'))
    username = session['username']
    query = "SELECT ID, CreditPoints FROM customer WHERE Name=%s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        customer_id = result['ID']
        credit_points = result['CreditPoints']
    else:
        flash('Could not retrieve customer information from database', 'error')
        return redirect(url_for('views.index'))
    order_date = datetime.now()
    products = []
    total_price = 0
    for product_id in session.get('cart', []):
        cursor.execute('SELECT * FROM product WHERE ID=%s', (product_id,))
        product = cursor.fetchone()
        if product:
            product['quantity'] = session['cart'].count(product_id)
            products.append(product)
            total_price += product['Price'] * product['quantity']
    if products:
        if total_price > credit_points:
            flash('You do not have enough credit points to place this order!', 'error')
            return redirect(url_for('views.cart'))
        credit_points -= total_price
        query = "UPDATE customer SET CreditPoints=%s WHERE ID=%s"
        cursor.execute(query, (credit_points, customer_id))
        query = "SELECT COALESCE(MAX(ID), 0) AS max_id FROM orders"
        cursor.execute(query)
        result = cursor.fetchone()
        order_id = result['max_id'] + 1
        query = "INSERT INTO orders (ID, CustomerID, OrderDate) VALUES (%s, %s, %s)"
        cursor.execute(query, (order_id, customer_id, order_date))
        for product in products:
            query = "SELECT COALESCE(MAX(ID), 0) AS max_id FROM orderitem"
            cursor.execute(query)
            result = cursor.fetchone()
            order_item_id = result['max_id'] + 1
            query = "INSERT INTO orderitem (ID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (order_item_id, order_id, product['ID'], product['quantity']))
        query = "SELECT COALESCE(MAX(ID), 0) AS max_id FROM transaction"
        cursor.execute(query)
        result = cursor.fetchone()
        trans_id = result['max_id'] + 1
        query = "INSERT INTO transaction (ID, CustomerID, Date, CreditPoints) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (trans_id, customer_id, order_date, -total_price))
        db_conn.connection.commit()
        session['cart'] = []
        flash('Your order has been placed!', 'success')
        return redirect(url_for('views.index'))
    flash('Your cart is empty!', 'error')
    return redirect(url_for('views.cart'))

@views.route('/cart/remove/<int:id>', methods=['POST'])
def remove_from_cart(id):
    # Funkce pro odstranění produktu z košíku
    if 'cart' not in session:
        session['cart'] = []

    if id not in session['cart']:
        flash('Product not found in cart', 'error')
        return redirect(url_for('views.cart'))

    session['cart'].remove(id)
    flash('Product removed from cart', 'success')
    return redirect(url_for('views.cart'))

@views.route('/order_history')
def order_history():
    # Funkce pro zobrazení historie objednávek
    db_conn = DbConnection.get_instance()
    cursor = db_conn.connection.cursor(dictionary=True)

    if 'username' not in session:
        flash('You need to log in to view your order history!', 'error')
        return redirect(url_for('views.login'))

    username = session['username']
    query = '''
        SELECT o.ID, o.OrderDate, oi.ProductID, oi.Quantity, t.CreditPoints
        FROM orders o
        INNER JOIN orderitem oi ON o.ID = oi.OrderID
        INNER JOIN transaction t ON oi.ID = t.ID
        INNER JOIN customer c ON o.CustomerID = c.ID
        WHERE c.Name = %s
    '''
    cursor.execute(query, (username,))
    order_history = cursor.fetchall()

    return render_template('order_history.php', order_history=order_history)

# Přidání filtru pro formátování cen
@views.app_template_filter('format_price')
def format_price(value):
    if value is None:
        return "0 Kč"
    return "{:,.2f}".format(value).replace(",", " ").replace(".00", "")
