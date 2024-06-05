"""
Dokumentace k testování - Testování třídy DbConnection

Tento soubor obsahuje jednotkové testy pro třídu DbConnection. Používáme knihovnu unittest pro testování singletonového vzoru v třídě DbConnection.

Třídy zahrnují:

1. TestDbConnection - Testovací třída pro DbConnection.
"""

import unittest
from unittest.mock import patch, MagicMock
from mysql.connector import Error
from db_connect import DbConnection

class TestDbConnection(unittest.TestCase):
    """
    Testovací třída pro DbConnection.

    Metody:
    - setUpClass(cls): Inicializuje instanci DbConnection pro testování.
    - test_singleton_pattern(): Testuje, zda třída DbConnection dodržuje singletonový vzor.
    """
    
    @classmethod
    def setUpClass(cls):
        # Inicializace instance DbConnection
        cls.db_connection = DbConnection.get_instance()

    def test_singleton_pattern(self):
        # Testování singletonového vzoru
        with self.assertRaises(Exception) as context:
            DbConnection()
        self.assertEqual(str(context.exception), "This class is a singleton!")

if __name__ == '__main__':
    unittest.main()
