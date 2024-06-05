"""
Autentizační modul pro Flask webovou aplikaci

Tento modul obsahuje funkce pro autentizaci uživatelů ve Flask webové aplikaci, včetně přihlašování, registrace, odhlášení a správy účtu.

Třídy a funkce:
- Blueprint 'auth': Definuje autentizační moduly.
- login(): Přihlašovací funkce.
- register(): Registrační funkce.
- logout(): Odhlášení uživatele.
- insert_user(): Vložení nového uživatele do databáze.
- account(): Správa uživatelského účtu.

"""

from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from src.db_connect import DbConnection
import re

# Vytvoření blueprintu pro autentizaci
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Funkce pro přihlášení uživatele
    if 'cart' not in session:
        session['cart'] = {} # Inicializace košíku, pokud není v session

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db_conn = DbConnection.get_instance()
        cursor = db_conn.connection.cursor()
        query = "SELECT * FROM customer WHERE Name = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            session['username'] = user[1] # Uložení uživatelského jména do session
            return redirect(url_for('views.index'))
        else:
            error = 'Invalid username or password'
            return render_template('auth.php', error=error)

    if 'username' in session:
        return redirect(url_for('views.index')) # Přesměrování na úvodní stránku, pokud je uživatel již přihlášen

    return render_template('auth.php')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # Funkce pro registraci nového uživatele
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        email = request.form.get('email')

        # Kontrola, že všechna pole jsou vyplněna
        if not all([username, password, confirm_password, email]):
            error = 'Please fill out all fields'
            return render_template('auth.php', error=error)

        # Kontrola, že hesla se shodují
        if password != confirm_password:
            error = 'Password and confirm password fields must match'
            return render_template('auth.php', error=error)

        # Kontrola, že uživatelské jméno není již použito
        db_conn = DbConnection.get_instance()
        cursor = db_conn.connection.cursor()
        query = "SELECT * FROM Customer WHERE Name = %s"
        values = (username,)
        cursor.execute(query, values)
        user = cursor.fetchone()
        if user:
            error = 'Username already taken'
            return render_template('auth.php', error=error)

        # Kontrola platnosti emailové adresy
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error = 'Invalid email address'
            return render_template('auth.php', error=error)

        # Vložení uživatele do databáze
        insert_user(username, password, email)

        flash('Registration successful! You can now log in.', category='success')
        return redirect(url_for('auth.login'))

    return render_template('auth.php')

@auth.route('/logout')
def logout():
    # Funkce pro odhlášení uživatele
    session.pop('cart', None) # Odstranění košíku ze session
    session.pop('username', None) # Odstranění uživatelského jména ze session

    return redirect(url_for('views.index'))

def insert_user(username, password, email, city="unknown", credit_points=10000.0, telephone="unknown"):
    # Funkce pro vložení nového uživatele do databáze
    db_conn = DbConnection.get_instance()
    cursor = db_conn.connection.cursor()

    cursor.execute("SELECT MAX(ID) FROM Customer")
    result = cursor.fetchone()
    next_id = (result[0] or 0) + 1

    query = "INSERT INTO Customer (ID, Name, City, CreditPoints, password, email, telephone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (next_id, username, city, credit_points, password, email, telephone)
    cursor.execute(query, values)
    db_conn.connection.commit()

@auth.route('/account', methods=['GET', 'POST'])
def account():
    # Funkce pro správu uživatelského účtu
    username = session.get('username')
    if not username:
        return redirect(url_for('auth.login')) # Přesměrování na přihlášení, pokud uživatel není přihlášen

    db_conn = DbConnection.get_instance()
    cursor = db_conn.connection.cursor()
    query = "SELECT City, CreditPoints, email, telephone FROM Customer WHERE Name = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    city, credit_points, email, telephone = result

    if request.method == 'POST':
        new_city = request.form['city']
        new_email = request.form['email']
        new_telephone = request.form['telephone']
        update_query = "UPDATE Customer SET City = %s, email = %s, telephone = %s WHERE Name = %s"
        cursor.execute(update_query, (new_city, new_email, new_telephone, username))
        db_conn.connection.commit()
        city = new_city
        email = new_email
        telephone = new_telephone

    return render_template('account.php', city=city, credit_points=credit_points, email=email, telephone=telephone)
