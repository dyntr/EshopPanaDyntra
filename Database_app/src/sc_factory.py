from db_connect import DbConnection
from db_factory import *
import csv
import os

import json
import xml.etree.ElementTree as ET


class Sc_Factory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()
        self.cursor = self.db_conn.connection.cursor()
        self.customer_factory = CustomerFactory()
        self.product_factory = ProductFactory()
        self.order_factory = OrdersFactory()
        self.order_item_factory = OrderItemFactory()
        self.transaction_factory = TransactionFactory()
        self.report_factory = GenerateReportFactory()

    def create_order(self, customer_id, order_date, products):
            cursor = self.db_conn.cursor()
            query = "SELECT MAX(ID) FROM Orders"
            cursor.execute(query)
            result = cursor.fetchone()
            next_order_id = 1 if result[0] is None else result[0] + 1
            query = "INSERT INTO orders (ID, CustomerID, OrderDate) VALUES (%s, %s, %s)"
            cursor.execute(query, (next_order_id, customer_id, order_date))
            self.db_conn.connection.commit()

            total_price = 0
            for product in products:
                product_id = product['id']
                quantity = product['quantity']
                query = "SELECT Price FROM product WHERE ID=%s"
                cursor.execute(query, (product_id,))
                result = cursor.fetchone()
                product_price = result[0]
                total_price += product_price * quantity

                query = "SELECT MAX(ID) FROM OrderItem"
                cursor.execute(query)
                result = cursor.fetchone()
                next_item_id = 1 if result[0] is None else result[0] + 1

                query = "INSERT INTO OrderItem (ID, OrderID, ProductID, Quantity) VALUES (%s, %s, %s, %s)"
                cursor.execute(
                    query, (next_item_id, next_order_id, product_id, quantity))

            query = "SELECT CreditPoints FROM Customer WHERE ID=%s"
            cursor.execute(query, (customer_id,))
            result = cursor.fetchone()
            current_credit_points = result[0]
            updated_credit_points = current_credit_points - total_price
            query = "UPDATE Customer SET CreditPoints=%s WHERE ID=%s"
            cursor.execute(query, (updated_credit_points, customer_id))

            query = "INSERT INTO Transaction (CustomerID, Date, CreditPoints) VALUES (%s, %s, -%s)"
            cursor.execute(query, (customer_id, order_date, total_price))

            self.db_conn.connection.commit()
            cursor.close()
            return next_order_id
    
    def create_menu_order(self):
                customer_id = int(input("\nEnter customer ID: "))
                order_date = input("Enter order date: ")
                products = []
                product = {}
                while True:
                    product_id = int(input("Enter product ID: "))
                    quantity = int(input("Enter quantity: "))
                    product = {'id': product_id, 'quantity': quantity}
                    products.append(product)
                    add_another = input("Do you want to add another product? (y/n)")
                    if add_another != 'y':
                        break
                order_id = self.create_order(customer_id, order_date, products)
                print("\nOrder created with ID: ", order_id)


class GenerateReportFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()
        self.cursor = self.db_conn.connection.cursor()

    def generate_report(self):

        self.cursor.execute("SELECT City, SUM(CreditPoints) AS TotalCreditPoints, COUNT(*) AS TotalCustomers "
                            "FROM Customer "
                            "GROUP BY City")
        customer_data = self.cursor.fetchall()

        self.cursor.execute("SELECT Type, SUM(Price * Quantity) AS TotalSales "
                            "FROM OrderItem "
                            "JOIN Product ON OrderItem.ProductID = Product.ID "
                            "GROUP BY Type")
        product_data = self.cursor.fetchall()

        report = "-----------------------------\n"
        report += "Summary Report\n"
        report += "-----------------------------\n\n"

        report += "Customer Data:\n"
        report += "City, Total Credit Points, Total Customers\n"
        for row in customer_data:
            report += f"{row[0]}, {row[1]}, {row[2]}\n"
        report += "\n"

        report += "Product Data:\n"
        report += "Type, Total Sales\n"
        for row in product_data:
            report += f"{row[0]}, {row[1]}\n"

        report += "-----------------------------\n"
        report += "End of Report\n"
        report += "-----------------------------\n"

        self.cursor.close()

        return report
    




class ImportFactory:
    def __init__(self):
        self.db_conn = DbConnection.get_instance()
        self.cursor = self.db_conn.connection.cursor()
        self.customer_factory = CustomerFactory()
        self.product_factory = ProductFactory()
        self.order_factory = OrdersFactory()
        self.order_item_factory = OrderItemFactory()
        self.transaction_factory = TransactionFactory()
        self.report_factory = GenerateReportFactory()

    def import_data(self):
        file_format = input("Enter the file format (csv, json, xml, xlsx): ")

        if file_format.lower() == "csv":
            file_name = input("Enter the file name: ")
            table_name = input("Enter the name of the table to import data to: ")
            file_path = "../data" + os.path.sep + file_name
            try:
                with open(file_path, 'r') as file:
                    reader = csv.reader(file)
                    header = next(reader)

                    if table_name.lower() == "customer":
                        for row in reader:
                            self.customer_factory.create_customer(row[0], row[1], row[2], row[3], row[4], row[5])
                    elif table_name.lower() == "product":
                        for row in reader:
                            self.product_factory.add_product(row[0], row[1], float(row[2]))
                    elif table_name.lower() == "order":
                        for row in reader:
                            self.order_factory.create_order(row[0], row[1], row[2])
                    elif table_name.lower() == "order item":
                        for row in reader:
                            self.order_item_factory.create_order_item(row[0], row[1], row[2])
                    elif table_name.lower() == "transaction":
                        for row in reader:
                            self.transaction_factory.create_transaction(row[0], row[1], row[2])
                    else:
                        print("Table not found.")
            except Exception as e:
                print("An error occurred while importing data:", e)
            else:
                print("Data imported successfully.")
                
        elif file_format.lower() == "json":
            file_name = input("Enter the file name: ")
            table_name = input("Enter the name of the table to import data to: ")
            file_path = "../data" + os.path.sep + file_name
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)

                    if table_name.lower() == "customer":
                        for row in data:
                            self.customer_factory.create_customer(row["Name"], row["City"], row["CreditPoints"], row["password"],row["email"], row["telephone"] )
                    elif table_name.lower() == "product":
                        for row in data:
                            self.product_factory.add_product(row["Name"], row["Type"], float(row["Price"]))
                    elif table_name.lower() == "order":
                        for row in data:
                            self.order_factory.create_order(row["CustomerID"], row["OrderDate"])
                    elif table_name.lower() == "order item":
                        for row in data:
                            self.order_item_factory.create_order_item(row["OrderID"], row["ProductID"], row["Quantity"])
                    elif table_name.lower() == "transaction":
                        for row in data:
                            self.transaction_factory.create_transaction(row["OrderID"], row["Date"], row["CreditPoints"])
                    else:
                        print("Table not found.")
            except Exception as e:
                print("An error occurred while importing data:", e)
            else:
                print("Data imported successfully.")
        elif file_format.lower() == "xml":
            file_name = input("Enter the file name: ")
            table_name = input("Enter the name of the table to import data to: ")
            file_path = "../data" + os.path.sep + file_name
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                for row in root:
                    if table_name.lower() == "customer":
                        name = row.find('Name').text
                        city = row.find('City').text
                        credit = row.find('CreditPoints').text
                        password = row.find('password')
                        email  = row.find('email')
                        telephone = row.find('telephone').text
                       
                        self.customer_factory.create_customer(name, city, credit , password ,email, telephone)
                    elif table_name.lower() == "product":
                        name = row.find('Name').text
                        type = row.find('Type').text
                        price = float(row.find('Price').text)
                        self.product_factory.add_product(name, type, price)
                    elif table_name.lower() == "orders":
                        customer_id = int(row.find('CustomerID').text)
                        date = row.find('OrderDate').text
                        self.order_factory.create_order(customer_id, date)
                    elif table_name.lower() == "orderitem":
                        order_id = int(row.find('OrderID').text)
                        product_id = int(row.find('ProductID').text)
                        quantity = int(row.find('Quantity').text)
                        self.order_item_factory.create_order_item(order_id, product_id , quantity)
                    elif table_name.lower() == "transaction":
                        customer_id = int(row.find('CustomerID').text)
                        date = row.find('Date').text
                        quantity = int(row.find('Quantity').text)
                        self.transaction_factory.create_transaction(customer_id ,date, quantity)
                    else:
                        print("Table not found.")
            except Exception as e:
                print("An error occurred while importing data:", e)
            else:
                print("Data imported successfully.")    
        