"""
Dokumentace k testování - Testování třídy Sc_Factory

Tento soubor obsahuje jednotkové testy pro třídu Sc_Factory. Používáme knihovnu unittest a mockování pro testování funkcí v interaktivním prostředí.

Třídy zahrnují:

1. TestScFactory - Testovací třída pro Sc_Factory.
"""

import unittest
from unittest import mock
from io import StringIO
from sc_factory import Sc_Factory
from db_connect import DbConnection

class TestScFactory(unittest.TestCase, Sc_Factory):
    """
    Testovací třída pro Sc_Factory.

    Metody:
    - test_create_menu_order(mock_stdout): Testuje interaktivní funkci create_menu_order.
    """

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_create_menu_order(self, mock_stdout):
        expected_output = 'Enter customer ID: \nEnter order date: \nEnter product ID: \nEnter quantity: \nDo you want to add another product? (y/n)\n\nOrder created with ID: 1\n'

        # Mocking user inputs for the function
        with mock.patch('builtins.input', side_effect=['1', '2022-01-01', '1', '5', 'n']):
            self.create_menu_order()

        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()