"""
Jednotkové testy pro Flask Web Application - E-shop

Tento soubor obsahuje jednotkové testy pro autentizaci ve Flask webové aplikaci e-shopu.
Používáme knihovnu unittest pro testování různých pohledů a funkcí.

Třídy zahrnují:

1. AuthTestCase - Testovací třída pro autentizační pohledy.
"""

import unittest
from flask import url_for
from __init__ import create_app
from src.db_connect import DbConnection

class AuthTestCase(unittest.TestCase):
    """
    Testovací třída pro autentizační pohledy.

    Metody:
    - setUp(): Inicializuje Flask aplikaci a testovací klient, připraví databázi.
    - tearDown(): Uzavře připojení k databázi po testech.
    - test_login(): Testuje přihlášení s platnými a neplatnými údaji.
    - test_register(): Testuje registraci nového uživatele a registraci s existujícím uživatelským jménem.
    - test_logout(): Testuje odhlášení a neoprávněný přístup po odhlášení.
    - test_login_with_invalid_credentials(): Testuje přihlášení s neplatnými údaji.
    - test_register_with_existing_username(): Testuje registraci s existujícím uživatelským jménem.
    - test_register_with_invalid_email(): Testuje registraci s neplatnou emailovou adresou.
    - test_account_update(): Testuje aktualizaci uživatelských údajů.
    """
    
    def setUp(self):
        # Inicializace Flask aplikace a testovacího klienta
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            DbConnection.init_db()

    def tearDown(self):
        # Uzavření připojení k databázi
        with self.app.app_context():
            DbConnection.close_db()

    def test_login(self):
        # Test s platnými přihlašovacími údaji
        response = self.client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, user1!', response.data)

        # Test s neplatnými přihlašovacími údaji
        response = self.client.post('/login', data=dict(username='user1', password='wrong_password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)

    def test_register(self):
        # Test s platnou registrací
        response = self.client.post('/register', data=dict(username='new_user', password='new_password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, new_user!', response.data)

        # Test s existujícím uživatelským jménem
        response = self.client.post('/register', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already exists', response.data)

    def test_logout(self):
        # Přihlášení nejprve
        response = self.client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Test odhlášení
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have been logged out', response.data)

        # Test neoprávněného přístupu po odhlášení
        response = self.client.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Unauthorized Access', response.data)

    def test_login_with_invalid_credentials(self):
        # Test s neplatnými přihlašovacími údaji
        response = self.client.post('/login', data=dict(username='user1', password='invalid_password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)

    def test_register_with_existing_username(self):
        # Test s existujícím uživatelským jménem
        response = self.client.post('/register', data=dict(username='user1', password='password', confirm_password='password', email='user1@example.com'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already taken', response.data)

    def test_register_with_invalid_email(self):
        # Test s neplatnou emailovou adresou
        response = self.client.post('/register', data=dict(username='new_user', password='password', confirm_password='password', email='invalid_email'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid email address', response.data)

    def test_account_update(self):
        # Test aktualizace uživatelských údajů
        with self.client as c:
            # Přihlášení nejprve
            c.post('/login', data=dict(username='user1', password='password1'))
            # Aktualizace údajů
            response = c.post('/account', data=dict(city='New York', email='new_email@example.com', telephone='1234567890'))
            self.assertEqual(response.status_code, 200)
            # Kontrola, že údaje byly aktualizovány v databázi
            with self.app.app_context():
                db_conn = DbConnection.get_instance()
                cursor = db_conn.connection.cursor()
                query = "SELECT City, email, telephone FROM Customer WHERE Name = %s"
                cursor.execute(query, ('user1',))
                result = cursor.fetchone()
                self.assertEqual(result, ('New York', 'new_email@example.com', '1234567890'))

    def test_account_update(self):
        # Přihlášení nejprve
        response = self.client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Test aktualizace účtu
        response = self.client.post('/account', data=dict(city='New York', email='new_email@example.com', telephone='1234567890'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account information updated', response.data)

        # Test, že informace o účtu byly aktualizovány v databázi
        with self.app.app_context():
            db_conn = DbConnection.get_instance()
            cursor = db_conn.connection.cursor()
            query = "SELECT City, email, telephone FROM Customer WHERE Name = %s"
            cursor.execute(query, ('user1',))
            result = cursor.fetchone()
            self.assertEqual(result, ('New York', 'new_email@example.com', '1234567890'))

if __name__ == '__main__':
    unittest.main()
