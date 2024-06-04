import unittest
from db_connect import DbConnection
from db_factory import CustomerFactory, ProductFactory, OrdersFactory

class TestFactories(unittest.TestCase):

    def setUp(self):
        self.db_conn = DbConnection.get_instance()
        self.cursor = self.db_conn.connection.cursor()
        self.customer_factory = CustomerFactory()
        self.product_factory = ProductFactory()
        self.order_factory = OrdersFactory()
    
    def tearDown(self):
        self.cursor.execute("DELETE FROM Customer")
        self.cursor.execute("DELETE FROM Product")
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
        customer = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        product = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_factory = OrdersFactory()
        order_factory.create_order(customer["ID"], product["ID"], 2)
        order = order_factory.get_order(1)
        self.assertEqual(order["CustomerID"], customer["ID"])
        self.assertEqual(order["ProductID"], product["ID"])
        self.assertEqual(order["Quantity"], 2)

    def test_get_order(self):
        customer = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        product = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_factory = OrdersFactory()
        order_factory.create_order(customer["ID"], product["ID"], 2)
        order = order_factory.get_order(1)
        self.assertEqual(order["CustomerID"], customer["ID"])
        self.assertEqual(order["ProductID"], product["ID"])
        self.assertEqual(order["Quantity"], 2)

    def test_update_order(self):
        customer = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        product = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_factory = OrdersFactory()
        order_factory.create_order(customer["ID"], product["ID"], 2)
        order_factory.update_order(1, customer["ID"], product["ID"], 3)
        order = order_factory.get_order(1)
        self.assertEqual(order["CustomerID"], customer["ID"])
        self.assertEqual(order["ProductID"], product["ID"])
        self.assertEqual(order["Quantity"], 3)

    def test_delete_order(self):
        customer = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        product = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_factory = OrdersFactory()
        order_factory.create_order(customer["ID"], product["ID"], 2)
        self.assertTrue(order_factory.delete_order(1))
        self.assertIsNone(order_factory.get_order(1))


    def test_update_order(self):
        customer = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        product = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_factory = OrdersFactory()
        order_factory.create_order(customer["ID"], product["ID"], 2)
        order_factory.update_order(1, product["ID"], 3)
        order = order_factory.get_order(1)
        self.assertEqual(order["CustomerID"], customer["ID"])
        self.assertEqual(order["ProductID"], product["ID"])
        self.assertEqual(order["Quantity"], 3)

    def test_delete_order(self):
        customer = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        product = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        order_factory = OrdersFactory()
        order_factory.create_order(customer["ID"], product["ID"], 2)
        self.assertTrue(order_factory.delete_order(1))
        self.assertIsNone(order_factory.get_order(1))

    def test_get_orders_by_customer(self):
        customer1 = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        customer2 = self.customer_factory.create_customer("Jane Doe", "Los Angeles", 200, "newpassword", "jane.doe@example.com")
        product1 = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        product2 = self.product_factory.add_product("Product 2", "Type 2", 20.0)
        order_factory = OrdersFactory()
        order_factory.create_order(customer1["ID"], product1["ID"], 2)
        order_factory.create_order(customer1["ID"], product2["ID"], 3)
        order_factory.create_order(customer2["ID"], product1["ID"], 1)
        orders = order_factory.get_orders_by_customer(customer1["ID"])
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0]["CustomerID"], customer1["ID"])
        self.assertEqual(orders[0]["ProductID"], product1["ID"])
        self.assertEqual(orders[0]["Quantity"], 2)
        self.assertEqual(orders[1]["CustomerID"], customer1["ID"])
        self.assertEqual(orders[1]["ProductID"], product2["ID"])
        self.assertEqual(orders[1]["Quantity"], 3) 



    def test_get_orders_by_customer(self):
        # create customers and products
        customer1 = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        customer2 = self.customer_factory.create_customer("Jane Doe", "Los Angeles", 200, "newpassword", "jane.doe@example.com")
        product1 = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        product2 = self.product_factory.add_product("Product 2", "Type 2", 20.0)
        # create orders for customers
        order_factory = OrdersFactory()
        order_factory.create_order(customer1["ID"], product1["ID"], 2)
        order_factory.create_order(customer1["ID"], product2["ID"], 3)
        order_factory.create_order(customer2["ID"], product1["ID"], 1)
        # get orders for customer1
        orders = order_factory.get_orders_by_customer(customer1["ID"])
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0]["Customer ID"], customer1["ID"])
        self.assertEqual(orders[1]["Customer ID"], customer1["ID"])
        # get orders for customer2
        orders = order_factory.get_orders_by_customer(customer2["ID"])
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["Customer ID"], customer2["ID"])

    def test_get_orders_by_product(self):
        # create customers and products
        customer1 = self.customer_factory.create_customer("John Doe", "New York", 100, "password", "john.doe@example.com")
        customer2 = self.customer_factory.create_customer("Jane Doe", "Los Angeles", 200, "newpassword", "jane.doe@example.com")
        product1 = self.product_factory.add_product("Product 1", "Type 1", 10.0)
        product2 = self.product_factory.add_product("Product 2", "Type 2", 20.0)
        # create orders for customers
        order_factory = OrdersFactory()
        order_factory.create_order(customer1["ID"], product1["ID"], 2)
        order_factory.create_order(customer1["ID"], product2["ID"], 3)
        order_factory.create_order(customer2["ID"], product1["ID"], 1)
        # get orders for product1
        orders = order_factory.get_orders_by_product(product1["ID"])
        self.assertEqual(len(orders), 2)
        self.assertEqual(orders[0]["Product ID"], product1["ID"])
        self.assertEqual(orders[1]["Product ID"], product1["ID"])
        # get orders for product2
        orders = order_factory.get_orders_by_product(product2["ID"])
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["Product ID"], product2["ID"])   
        
           
if __name__ == '__main__':
   unittest.main()        