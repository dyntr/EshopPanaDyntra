
from db_connect import DbConnection
import mysql


class CustomerFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()
        self.cursor = self.db_conn.connection.cursor()

    def create_customer(self, name, city, credit_points, password, email):
        # Validate credit points
        try:
            credit_points = float(credit_points)
            if credit_points < 0:
                raise ValueError("Credit points must be non-negative")
        except ValueError as e:
            raise Exception("Invalid credit points: " + str(e))

        # Check if customer exists
        if self._customer_exists(name, city):
            raise Exception("Customer with the same name and city already exists")

        # Insert new customer
        next_id = self._get_next_id()
        query = "INSERT INTO Customer (ID, Name, City, CreditPoints, password, email) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (next_id, name, city, credit_points, password, email))
        self.db_conn.connection.commit()
        return True

    def read_customer(self, customer_id):
        self.cursor.execute(
            "SELECT * FROM Customer WHERE ID = %s",
            (customer_id,)
        )
        return self.cursor.fetchone()

    def update_customer(self, id, name, city, credit_points, password, email):
        # Validate credit points
        try:
            credit_points = float(credit_points)
            if credit_points < 0:
                raise ValueError("Credit points must be non-negative")
        except ValueError as e:
            raise Exception("Invalid credit points: " + str(e))

        # Check if customer exists
        if not self._customer_exists(id):
            raise Exception("Customer not found")

        # Update customer
        self.cursor.execute(
            "UPDATE Customer SET Name = %s, City = %s, CreditPoints = %s, password = %s, email = %s WHERE ID = %s",
            (name, city, credit_points, password, email, id)
        )
        self.db_conn.connection.commit()

    def delete_customer(self, id):
        # Check if customer exists
        if not self._customer_exists_by_id(id):
            return False

        # Delete customer
        try:
            query = "DELETE FROM Customer WHERE ID=%s"
            self.cursor.execute(query, (id,))
            self.db_conn.connection.commit()
            rowcount = self.cursor.rowcount
            return rowcount > 0
        except mysql.connector.errors.IntegrityError as e:
            if e.errno == 1451:
                raise Exception(
                    "Cannot delete customer, there are orders associated with it.")
            else:
                raise e

    def _get_next_id(self):
        query = "SELECT MAX(ID) FROM Customer"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return 1 if result[0] is None else result[0] + 1

    def _customer_exists(self, name, city):
        query = "SELECT * FROM Customer WHERE Name = %s AND City = %s"
        self.cursor.execute(query, (name, city))
        return self.cursor.fetchone() is not None

    def _customer_exists_by_id(self, customer_id):
        query = "SELECT * FROM Customer WHERE ID = %s"
        self.cursor.execute(query, (customer_id,))
        return self.cursor.fetchone() is not None


class ProductFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()
    
    
    def get_next_id(self):
        cursor = self.db_conn.cursor()
        query = "SELECT MAX(ID) FROM Product"
        cursor.execute(query)
        result = cursor.fetchone()
        next_id = 1 if result[0] is None else result[0] + 1
        cursor.close()
        return next_id
    
    def add_product(self, name, type, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")

        cursor = self.db_conn.cursor()
        query = "SELECT MAX(ID) FROM Product"
        cursor.execute(query)
        result = cursor.fetchone()
        next_id = 1 if result[0] is None else result[0] + 1

        query = "INSERT INTO Product(ID, Name, Type, Price) VALUES(%s, %s, %s, %s)"
        cursor.execute(query, (next_id, name, type, price))
        self.db_conn.connection.commit()
        cursor.close()
        return True

    def get_product(self, product_id: int):
        cursor = self.db_conn.cursor()
        query = "SELECT * FROM Product WHERE ID = %s"
        cursor.execute(query, (product_id,))
        product = cursor.fetchone()
        cursor.close()
        return product

    def update_product(self, id, name=None, type=None, price=None):
        if price is not None and price < 0:
            raise ValueError("Price cannot be negative.")

        cursor = self.db_conn.cursor()
        query = "UPDATE Product SET Name=%s, Type=%s, Price=%s WHERE ID=%s"
        cursor.execute(query, (name, type, price, id))
        self.db_conn.connection.commit()
        cursor.close()

    def delete_product(self, id):
        if not self._product_exists(id):
            return False

        cursor = self.db_conn.cursor()

        query = "DELETE FROM OrderItem WHERE ProductID=%s"
        cursor.execute(query, (id,))
        self.db_conn.connection.commit()

        query = "DELETE FROM Product WHERE ID=%s"
        cursor.execute(query, (id,))
        self.db_conn.connection.commit()
        cursor.close()
        return True

    def _product_exists(self, id):
        cursor = self.db_conn.cursor()
        query = "SELECT * FROM Product WHERE ID=%s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        return bool(result)
    
    

class OrdersFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()

    def create_order(self, customer_id, order_date):
        cursor = self.db_conn.cursor()
        query = "INSERT INTO orders (CustomerID, OrderDate) VALUES (%s, %s)"
        cursor.execute(query, (customer_id, order_date))
        self.db_conn.connection.commit()
        next_order_id = cursor.lastrowid
        cursor.close()
        return next_order_id

    def update_order(self, order_id: int, customer_id: int, order_date: str) -> bool:
        cursor = self.db_conn.cursor()
        query = "UPDATE orders SET Customer_ID = %s, OrderDate = %s WHERE ID = %s"
        cursor.execute(query, (customer_id, order_date, order_id))
        self.db_conn.connection.commit()
        return cursor.rowcount == 1

    def delete_order(self, id):
        cursor = self.db_conn.cursor()

        query = "DELETE FROM OrderItem WHERE OrderID=%s"
        cursor.execute(query, (id,))
        self.db_conn.connection.commit()

        query = "DELETE FROM orders WHERE ID=%s"
        cursor.execute(query, (id,))
        self.db_conn.connection.commit()

        deleted = cursor.rowcount > 0
        cursor.close()
        return deleted

    def get_order(self, order_id: int) -> dict:
        cursor = self.db_conn.cursor()
        query = "SELECT * FROM orders WHERE ID = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        if result:
            return {"id": result[0], "customer_id": result[1], "order_date": result[2]}
        else:
            return None


class OrderItemFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()

    def create_order_item(self, order_id, product_id, quantity):
        cursor = self.db_conn.cursor()
        query = "SELECT MAX(ID) FROM OrderItem"
        cursor.execute(query)
        result = cursor.fetchone()
        next_id = 1 if result[0] is None else result[0] + 1
        cursor.execute(
            "INSERT INTO OrderItem (ID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)",
            (next_id, order_id, product_id, quantity)
        )
        self.db_conn.connection.commit()
        cursor.close()
        return next_id

    def read_order_item(self, order_item_id):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "SELECT * FROM OrderItem WHERE ID = %s",
            (order_item_id,)
        )
        return cursor.fetchone()

    def update_order_item(self, order_item_id, order_id, product_id, quantity):
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE OrderItem SET OrderID = %s, ProductID = %s, Quantity = %s WHERE ID = %s",
            (order_id, product_id, quantity, order_item_id)
        )
        self.db_conn.connection.commit()

    def delete_order_item(self, order_item_id):
        cursor = self.db_conn.cursor()

        query = "SELECT * FROM OrderItem WHERE ID=%s"
        cursor.execute(query, (order_item_id,))
        result = cursor.fetchone()
        if not result:
            cursor.close()
            return False

        query = "DELETE FROM OrderItem WHERE ID=%s"
        cursor.execute(query, (order_item_id,))
        self.db_conn.connection.commit()

        cursor.close()
        return True


class TransactionFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()
        self.cursor = self.db_conn.connection.cursor()

    def create_transaction(self, customer_id, date, credit_points):
        query = "SELECT MAX(ID) FROM Transaction"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        next_id = 1 if result[0] is None else result[0] + 1
        self.cursor.execute(
            "INSERT INTO Transaction (ID, CustomerID, Date, CreditPoints) VALUES (%s,%s, %s, %s)",
            (next_id, customer_id, date, credit_points)
        )
        self.db_conn.connection.commit()

    def read_transaction(self, transaction_id):
        self.cursor.execute(
            "SELECT * FROM Transaction WHERE ID = %s",
            (transaction_id,)
        )
        return self.cursor.fetchone()

    def update_transaction(self, transaction_id, customer_id, date, credit_points):
        self.cursor.execute(
            "UPDATE Transaction SET CustomerID = %s, Date = %s, CreditPoints = %s WHERE ID = %s",
            (customer_id, date, credit_points, transaction_id)
        )
        self.db_conn.connection.commit()

    def delete_transaction(self, transaction_id):

        query = "SELECT * FROM Transaction WHERE ID=%s"
        self.cursor.execute(query, (transaction_id,))
        result = self.cursor.fetchone()
        if not result:
            self.cursor.close()
            return False

        self.cursor.execute(
            "DELETE FROM Transaction WHERE ID = %s",
            (transaction_id,)
        )
        self.db_conn.connection.commit()



