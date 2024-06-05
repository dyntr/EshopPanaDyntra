"""
Jednotkové testy pro Flask Web Application - E-shop

Tento soubor obsahuje jednotkové testy pro Flask webovou aplikaci e-shopu. Používáme knihovnu unittest pro testování různých pohledů a funkcí.

Třídy zahrnují:

1. TestViews - Testovací třída pro Flask pohledy.
"""

import unittest
from flask import Flask
from views import views

class TestViews(unittest.TestCase):
    """
    Testovací třída pro Flask pohledy.

    Metody:
    - setUp(): Inicializuje Flask aplikaci a testovací klient.
    - test_home(): Testuje přesměrování na úvodní stránku.
    - test_login(): Testuje zobrazení přihlašovací stránky.
    - test_register(): Testuje zobrazení registrační stránky.
    - test_index_GET(): Testuje zobrazení úvodní stránky pomocí GET metody.
    - test_index_POST(): Testuje filtrování produktů pomocí POST metody.
    - test_products(): Testuje zobrazení seznamu produktů.
    - test_products_by_type(): Testuje zobrazení produktů podle typu.
    - test_search(): Testuje vyhledávání produktů.
    - test_add_to_cart(): Testuje přidání produktu do košíku.
    - test_cart(): Testuje zobrazení obsahu košíku.
    - test_buy(): Testuje vytvoření objednávky.
    - test_edit_profile_GET(): Testuje zobrazení stránky pro úpravu profilu.
    - test_edit_profile_POST(): Testuje aktualizaci uživatelského profilu.
    - test_logout(): Testuje odhlášení uživatele.
    - test_checkout_GET(): Testuje zobrazení stránky pro dokončení objednávky.
    - test_checkout_POST(): Testuje dokončení objednávky.
    - test_empty_cart(): Testuje zobrazení prázdného košíku.
    - test_remove_from_cart(): Testuje odstranění produktu z košíku.
    - test_invalid_checkout(): Testuje neplatné dokončení objednávky.
    - test_add_to_wishlist(): Testuje přidání produktu do seznamu přání.
    - test_remove_from_wishlist(): Testuje odstranění produktu ze seznamu přání.
    - test_empty_wishlist(): Testuje zobrazení prázdného seznamu přání.
    - test_wishlist(): Testuje zobrazení seznamu přání.
    - test_invalid_login(): Testuje neplatné přihlášení.
    - test_invalid_registration(): Testuje neplatnou registraci.
    """
    
    def setUp(self):
        # Inicializace Flask aplikace a testovacího klienta
        self.app = Flask(__name__)
        self.app.register_blueprint(views)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_home(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], 'http://localhost/')

    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Login</title>', response.data)

    def test_register(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Sign Up</title>', response.data)

    def test_index_GET(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to our online store</h1>', response.data)

    def test_index_POST(self):
        response = self.client.post('/', data={
            'min-price': '10',
            'max-price': '20',
            'price': 'asc'
        })
        self.assertEqual(response.status_code, 200)

    def test_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_products_by_type(self):
        response = self.client.get('/products_by_type/Clothing')
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.get('/search?q=shirt')
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = []
            response = self.client.post('/add_to_cart', data={'product_id': 1})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(c.session['cart']), 1)

    def test_cart(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = [1, 2]
            response = self.client.get('/cart')
            self.assertEqual(response.status_code, 200)

    def test_buy(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = [1, 2]
                sess['username'] = 'test_user'
            response = self.client.post('/buy')
            self.assertEqual(response.status_code, 302)
    
    def test_edit_profile_GET(self):
        response = self.client.get('/edit_profile')
        self.assertEqual(response.status_code, 302)

    def test_edit_profile_POST(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test_user'
            response = self.client.post('/edit_profile', data={
                'username': 'new_test_user',
                'email': 'new_test_user@example.com',
                'password': 'newpassword'
            })
            self.assertEqual(response.status_code, 302)
            self.assertEqual(c.session['username'], 'new_test_user')

    def test_logout(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test_user'
            response = self.client.get('/logout')
            self.assertEqual(response.status_code, 302)
            self.assertNotIn('username', c.session)

    def test_checkout_GET(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = [1, 2]
            response = self.client.get('/checkout')
            self.assertEqual(response.status_code, 302)

    def test_checkout_POST(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = [1, 2]
                sess['username'] = 'test_user'
            response = self.client.post('/checkout', data={
                'card_number': '1234-5678-9012-3456',
                'expiry_date': '12/24',
                'cvv': '123'
            })
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(c.session['cart']), 0)
    
    def test_empty_cart(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = []
            response = self.client.get('/cart')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your cart is empty', response.data)

    def test_remove_from_cart(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = [1, 2]
            response = self.client.post('/remove_from_cart', data={'product_id': 1})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(c.session['cart']), 1)

    def test_invalid_checkout(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['cart'] = [1, 2]
                sess['username'] = 'test_user'
            response = self.client.post('/checkout', data={
                'card_number': 'invalid-card-number',
                'expiry_date': '12/24',
                'cvv': '123'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Invalid credit card number', response.data)

    def test_add_to_wishlist(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['wishlist'] = []
            response = self.client.post('/add_to_wishlist', data={'product_id': 1})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(c.session['wishlist']), 1)

    def test_remove_from_wishlist(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['wishlist'] = [1, 2]
            response = self.client.post('/remove_from_wishlist', data={'product_id': 1})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(len(c.session['wishlist']), 1)

    def test_empty_wishlist(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['wishlist'] = []
            response = self.client.get('/wishlist')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your wishlist is empty', response.data)

    def test_wishlist(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['wishlist'] = [1, 2]
            response = self.client.get('/wishlist')
            self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post('/login', data={
            'username': 'invalid_username',
            'password': 'invalid_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)

    def test_invalid_registration(self):
        response = self.client.post('/register', data={
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username or email already exists', response.data)

if __name__ == '__main__':
    unittest.main()
