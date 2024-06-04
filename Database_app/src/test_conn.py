import unittest
from unittest.mock import patch, MagicMock
from mysql.connector import Error
from db_connect import DbConnection


class TestDbConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_connection = DbConnection.get_instance()

    def test_singleton_pattern(self):
        with self.assertRaises(Exception) as context:
            DbConnection()
        self.assertEqual(str(context.exception), "This class is a singleton!")

   
    
if __name__ == '__main__':
   unittest.main()               