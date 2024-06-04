import unittest
from flask import url_for
from __init__ import create_app
from src.db_connect import DbConnection

class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            DbConnection.init_db()

    def tearDown(self):
        with self.app.app_context():
            DbConnection.close_db()

    def test_login(self):
        # Test with valid credentials
        response = self.client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, user1!', response.data)

        # Test with invalid credentials
        response = self.client.post('/login', data=dict(username='user1', password='wrong_password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)

    def test_register(self):
        # Test with valid registration
        response = self.client.post('/register', data=dict(username='new_user', password='new_password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, new_user!', response.data)

        # Test with existing username
        response = self.client.post('/register', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already exists', response.data)

    def test_logout(self):
        # Login first
        response = self.client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Test logout
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You have been logged out', response.data)

        # Test unauthorized access after logout
        response = self.client.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 401)
        self.assertIn(b'Unauthorized Access', response.data)

    def test_login_with_invalid_credentials(self):
        # Test with invalid credentials
        response = self.client.post('/login', data=dict(username='user1', password='invalid_password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username or password', response.data)

    def test_register_with_existing_username(self):
        # Test with an existing username
        response = self.client.post('/register', data=dict(username='user1', password='password', confirm_password='password', email='user1@example.com'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already taken', response.data)

    def test_register_with_invalid_email(self):
        # Test with an invalid email address
        response = self.client.post('/register', data=dict(username='new_user', password='password', confirm_password='password', email='invalid_email'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid email address', response.data)

    def test_logout(self):
        # Test logout
        with self.client.session_transaction() as session:
            session['username'] = 'user1'
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'user1', response.data)


    def test_register_with_existing_username(self):
        # Test registration with an existing username
        response = self.client.post('/register', data=dict(username='user1', password='password1', confirm_password='password1', email='user1@example.com'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already taken', response.data)

    def test_register_with_invalid_email(self):
        # Test registration with an invalid email
        response = self.client.post('/register', data=dict(username='new_user', password='password1', confirm_password='password1', email='invalid_email'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid email address', response.data)

    def test_account_update(self):
        # Test updating user account information
        with self.client as c:
            # Login first
            c.post('/login', data=dict(username='user1', password='password1'))
            # Update account info
            response = c.post('/account', data=dict(city='New York', email='new_email@example.com', telephone='1234567890'))
            self.assertEqual(response.status_code, 200)
            # Check that the account info was updated in the database
            with self.app.app_context():
                db_conn = DbConnection.get_instance()
                cursor = db_conn.connection.cursor()
                query = "SELECT City, email, telephone FROM Customer WHERE Name = %s"
                cursor.execute(query, ('user1',))
                result = cursor.fetchone()
                self.assertEqual(result, ('New York', 'new_email@example.com', '1234567890'))

    def test_account_update(self):
        # Login first
        response = self.client.post('/login', data=dict(username='user1', password='password1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        # Test account update
        response = self.client.post('/account', data=dict(city='New York', email='new_email@example.com', telephone='1234567890'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account information updated', response.data)

        # Test that account information was updated in the database
        with self.app.app_context():
            db_conn = DbConnection.get_instance()
            cursor = db_conn.connection.cursor()
            query = "SELECT City, email, telephone FROM Customer WHERE Name = %s"
            cursor.execute(query, ('user1',))
            result = cursor.fetchone()
            self.assertEqual(result, ('New York', 'new_email@example.com', '1234567890'))                 
if __name__ == '__main__':
   unittest.main()