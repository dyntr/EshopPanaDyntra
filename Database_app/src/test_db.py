"""
Dokumentace k testování - Testování továrních tříd

Tento soubor obsahuje jednotkové testy pro tovární třídy CustomerFactory, ProductFactory a OrdersFactory. Používáme knihovnu unittest pro testování různých operací na databázových entitách.

Třídy zahrnují:

1. TestFactories - Testovací třída pro tovární třídy CustomerFactory, ProductFactory a OrdersFactory.
"""

import unittest
from db_connect import DbConnection
from db_factory import CustomerFactory, ProductFactory, OrdersFactory

class TestFactories(unittest.TestCase):
    """
    Testovací třída pro tovární třídy CustomerFactory, ProductFactory a OrdersFactory.

    Metody:
    - setUp(): Inicializuje připojení k databázi a továrny pro testování.
    - tearDown(): Vymaže data z testovacích tabulek po každém testu.
    - test_create_customer(): Testuje vytvoření zákazníka.
    - test_read_customer(): Testuje načtení zákazníka podle ID.
    - test_update_customer(): Testuje aktualizaci zákazníka.
    - test_delete_customer(): Testuje smazání zákazníka.
    - test_add_product(): Testuje přidání produktu.
    - test_get_product(): Testuje načtení produktu podle ID.
    - test_update_product(): Testuje aktualizaci produktu.
    - test_delete_product(): Testuje smazání produktu.
    - test_create_order(): Testuje vytvoření objednávky.
    - test_get_order(): Testuje načtení objednávky podle ID.
    - test_update_order(): Testuje aktualizaci objednávky.
    - test_delete_order(): Testuje smazání objednávky.
    - test_get_orders_by_customer(): Testuje načtení objednávek podle zákazníka.
    - test_get_orders_by_product(): Testuje načtení objednávek podle produktu.
    """
    
    def setUp(self):
        # Inicializace připojení k databázi a továrny pro testování
        self.db_conn = DbConnection.get_instance()
        self.cursor = self.db_conn.connection.cursor()
        self.customer_factory = CustomerFactory()
        self.product_factory = ProductFactory()
        self.order_factory = OrdersFactory()
    
    def tearDown(self):
        # Vymazání dat z testovacích tabulek po každém testu
        self.cursor.execute("DELETE FROM Customer")
        self.cursor.execute("DELETE FROM Product")
        self.cursor.execute("DELETE FROM Orders")
        self.cursor.execute("DELETE FROM OrderItem")
        self.db_conn.connection.commit()

    def test_create_customer(self):
        self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        customer = self.customer_factory.read_customer(1)
        self.assertEqual(customer["Name"], "John Doe")
        self.assertEqual(customer["City"], "New York")
        self.assertEqual(customer["CreditPoints"], 100.0)
        self.assertEqual(customer["password"], "password")
        self.assertEqual(customer["email"], "john.doe@example.com")

    def test_read_customer(self):
        self.cursor.execute("INSERT INTO Customer (ID, Name, City, CreditPoints, password, email) VALUES (1, 'John Doe', 'New York', 100, 'password', 'john.doe@example.com')")
        self.db_conn.connection.commit()
        customer = self.customer_factory.read_customer(1)
        self.assertEqual(customer["Name"], "John Doe")
        self.assertEqual(customer["City"], "New York")
        self.assertEqual(customer["CreditPoints"], 100.0)
        self.assertEqual(customer["password"], "password")
        self.assertEqual(customer["email"], "john.doe@example.com")

    def test_update_customer(self):
        self.cursor.execute("INSERT INTO Customer (ID, Name, City, CreditPoints, password, email) VALUES (1, 'John Doe', 'New York', 100, 'password', 'john.doe@example.com')")
        self.db_conn.connection.commit()
        self.customer_factory.update_customer(1, "Jane Doe", "Los Angeles", 200, "newpassword", "jane.doe@example.com")
        customer = self.customer_factory.read_customer(1)
        self.assertEqual(customer["Name"], "Jane Doe")
        self.assertEqual(customer["City"], "Los Angeles")
        self.assertEqual(customer["CreditPoints"], 200.0)
        self.assertEqual(customer["password"], "newpassword")
        self.assertEqual(customer["email"], "jane.doe@example.com")
    
    def test_delete_customer(self):
        self.cursor.execute("INSERT INTO Customer (ID, Name, City, CreditPoints, password, email) VALUES (1, 'John Doe', 'New York', 100, 'password', 'john.doe@example.com')")
        self.db_conn.connection.commit()
        self.assertTrue(self.customer_factory.delete_customer(1))
        self.assertIsNone(self.customer_factory.read_customer(1))

    def test_add_product(self):
        self.product_factory.add_product("Product 1", "Type 1", 10.0)
        product = self.product_factory.get_product(1)
        self.assertEqual(product["Name"], "Product 1")
        self.assertEqual(product["Type"], "Type 1")
        self.assertEqual(product["Price"], 10.0)

    def test_get_product(self):
        self.cursor.execute("INSERT INTO Product (ID, Name, Type, Price) VALUES (1, 'Product 1', 'Type 1', 10.0)")
        self.db_conn.connection.commit()
        product = self.product_factory.get_product(1)
        self.assertEqual(product["Name"], "Product 1")
        self.assertEqual(product["Type"], "Type 1")
        self.assertEqual(product["Price"], 10.0)

    def test_update_product(self):
        self.cursor.execute("INSERT INTO Product (ID, Name, Type, Price) VALUES (1, 'Product 1', 'Type 1', 10.0)")
        self.db_conn.connection.commit()
        self.product_factory.update_product(1, "Product 2", "Type 2", 20.0)
        product = self.product_factory.get_product(1)
        self.assertEqual(product["Name"], "Product 2")
        self.assertEqual(product["Type"], "Type 2")
        self.assertEqual(product["Price"], 20.0)

    def test_delete_product(self):
        self.cursor.execute("INSERT INTO Product (ID, Name, Type, Price) VALUES (1, 'Product 1', 'Type 1', 10.0)")
        self.db_conn.connection.commit()
        self.assertTrue(self.product_factory.delete_product(1))
        self.assertIsNone(self.product_factory.get_product(1))
    
    def test_create_order(self):
        self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_id = self.order_factory.create_order(1, "2022-01-01")
        self.order_factory.create_order_item(order_id, 1, 2)
        order = self.order_factory.get_order(order_id)
        self.assertEqual(order["CustomerID"], 1)
        order_items = self.order_factory.get_order_items(order_id)
        self.assertEqual(order_items[0]["ProductID"], 1)
        self.assertEqual(order_items[0]["Quantity"], 2)

    def test_get_order(self):
        self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_id = self.order_factory.create_order(1, "2022-01-01")
        self.order_factory.create_order_item(order_id, 1, 2)
        order = self.order_factory.get_order(order_id)
        self.assertEqual(order["CustomerID"], 1)
        order_items = self.order_factory.get_order_items(order_id)
        self.assertEqual(order_items[0]["ProductID"], 1)
        self.assertEqual(order_items[0]["Quantity"], 2)

    def test_update_order(self):
        self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_id = self.order_factory.create_order(1, "2022-01-01")
        self.order_factory.create_order_item(order_id, 1, 2)
        self.order_factory.update_order(order_id, 1, "2022-02-02")
        order = self.order_factory.get_order(order_id)
        self.assertEqual(order["CustomerID"], 1)
        self.assertEqual(order["OrderDate"], "2022-02-02")

    def test_delete_order(self):
        self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_id = self.order_factory.create_order(1, "2022-01-01")
        self.order_factory.create_order_item(order_id, 1, 2)
        self.assertTrue(self.order_factory.delete_order(order_id))
        self.assertIsNone(self.order_factory.get_order(order_id))

    def test_get_orders_by_customer(self):
        # Create customers and products
        self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        self.customer_factory.create_customer("Jane Doe", "Los Angeles", 200, "newpassword", "jane.doe@example.com")
        self.product_factory.add_product("Product 1", "Type 1", 10.0)
        self.product_factory.add_product("Product 2", "Type 2", 20.0)
        # Create orders for customers
        order_id1 = self.order_factory.create_order(1, "2022-01-01")
        self.order_factory.create_order_item(order_id1, 1, 2)
        order_id2 = self.order_factory.create_order(1, "2022-02-02")
        self.order_factory.create_order_item(order_id2, 2, 3)
        order_id3 = self.order_factory.create_order(2, "2022-03-03")
        self.order_factory.create_order_item(order_id3, 1, 1)
        # Get orders for customer1
        orders = self.order_factory.get_orders_by_customer(1)
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0]["CustomerID"], 1)
        self.assertEqual(orders[1]["CustomerID"], 1)
        # Get orders for customer2
        orders = self.order_factory.get_orders_by_customer(2)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["CustomerID"], 2)

    def test_get_orders_by_product(self):
        # Create customers and products
        self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        self.customer_factory.create_customer("Jane Doe", "Los Angeles", 200, "newpassword", "jane.doe@example.com")
        self.product_factory.add_product("Product 1", "Type 1", 10.0)
        self.product_factory.add_product("Product 2", "Type 2", 20.0)
        # Create orders for customers
        order_id1 = self.order_factory.create_order(1, "2022-01-01")
        self.order_factory.create_order_item(order_id1, 1, 2)
        order_id2 = self.order_factory.create_order(1, "2022-02-02")
        self.order_factory.create_order_item(order_id2, 2, 3)
        order_id3 = self.order_factory.create_order(2, "2022-03-03")
        self.order_factory.create_order_item(order_id3, 1, 1)
        # Get orders for product1
        orders = self.order_factory.get_orders_by_product(1)
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0]["ProductID"], 1)
        self.assertEqual(orders[1]["ProductID"], 1)
        # Get orders for product2
        orders = self.order_factory.get_orders_by_product(2)
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["ProductID"], 2)

if __name__ == '__main__':
    unittest.main()
