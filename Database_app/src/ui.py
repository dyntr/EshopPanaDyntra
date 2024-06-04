from db_factory import *
from sc_factory import *


class UI:
    def __init__(self):
        self.customer_factory = CustomerFactory()
        self.product_factory = ProductFactory()
        self.order_factory = OrdersFactory()
        self.order_item_factory = OrderItemFactory()
        self.transaction_factory = TransactionFactory()
        self.report_factory = GenerateReportFactory()
        self.sc_factory = Sc_Factory()
        self.import_factory = ImportFactory()
       
    def menu(self):
        while True:
            print("\nWelcome to the e-shop application")
            print("0. Create Order")
            print("1. Customers table")
            print("2. Products table")
            print("3. Orders table")
            print("4. Order Items table")
            print("5. Transactions table")
            print("6. Generate report")
            print("7. Import data")
            print("8. Exit")
            choice = input("Enter your choice: ")
            

            if choice == "0":
                self.sc_factory.create_menu_order()
            elif choice == "1":
                self.customer_menu()
            elif choice == "2":
                self.product_menu()
            elif choice == "3":
                self.order_menu()
            elif choice == "4":
                self.order_item_menu()
            elif choice == "5":
                self.transaction_menu() 
            elif choice == "6":
                report = self.report_factory.generate_report()
                print(report)
            elif choice == "7":
                data_import = self.import_factory.import_data()
                print(data_import)
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")

    def customer_menu(self):
        while True:
            print("\n--- Customer menu ---")
            print("1. Create new customer")
            print("2. Read customer details")
            print("3. Update customer details")
            print("4. Delete customer")
            print("5. Go back")
            choice = input("\nEnter your choice: ")
            
        
            if choice == "1":
                name = input("\nEnter name: ")
                city = input("Enter city: ")
                credit_points = int(input("Enter credit points: "))
                password = input("Enter password: ")
                email = input("Enter email: ")
                self.customer_factory.create_customer(name, city, credit_points, password, email)
                print("\nCustomer created successfully!")
            elif choice == "2":
                customer_id = int(input("Enter customer ID: "))
                customer = self.customer_factory.read_customer(customer_id)
                if customer:
                    print("ID: ", customer[0])
                    print("Name: ", customer[1])
                    print("City: ", customer[2])
                    print("Credit Points: ", customer[3])
                    print("password: ", customer[4])
                    print("email: ", customer[5])
                else:
                    print("Customer not found!")
            elif choice == "3":
                customer_id = int(input("\nEnter customer ID: "))
                customer = self.customer_factory.read_customer(customer_id)
                if customer:
                    name = input("Enter new name: ")
                    city = input("Enter new city: ")
                    credit_points = input("Enter new credit points : ")
                    password = input("Enter new password: ")
                    email = input("Enter new email: ")
                    self.customer_factory.update_customer(customer_id, name, city, credit_points, password, email)
                    print("Customer updated successfully!")
                else:
                    print("Customer not found!")
            elif choice == "4":
                customer_id = int(input("\nEnter customer ID: "))
                try:
                    if self.customer_factory.delete_customer(customer_id):
                        print("Customer deleted successfully")
                except Exception as e:
                    print(str(e))
                else:
                    print("Customer not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")

    def product_menu(self):
        while True:
            print("\n--- Product menu ---")
            print("1. Create new product")
            print("2. Read product details")
            print("3. Update product details")
            print("4. Delete product")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                name = input("\nEnter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                self.product_factory.add_product(name, description, price)
                print("Product created successfully!")
            elif choice == "2":
                product_id = int(input("\n5Enter product ID: "))
                product = self.product_factory.get_product(product_id)
                if product:
                    print("ID: ", product[0])
                    print("Name: ", product[1])
                    print("Description: ", product[2])
                    print("Price: ", product[3])
                else:
                    print("Product not found!")
            elif choice == "3":
                product_id = int(input("\nEnter product ID: "))
                product = self.product_factory.get_product(product_id)
                if product:
                    product_data = {"id": product[0], "name": product[1], "description": product[2], "price": product[3]}
                    name = input("\nEnter new name : ")
                    description = input("Enter new description : ")
                    price = input("Enter new price : ")
                    if name:
                        product_data["name"] = name
                    if description:
                        product_data["description"] = description
                    if price:
                        product_data["price"] = price
                    self.product_factory.update_product(product_data["id"], product_data["name"], product_data["description"], product_data["price"])
                    print("Product updated successfully!")
                else:
                    print("Product not found!")
            elif choice == "4":
                product_id = int(input("\nEnter product ID: "))
                if self.product_factory.delete_product(product_id):
                    print("Product deleted successfully!")
                else:
                    print("Product not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")   


    def order_menu(self):
        while True:
            print("\n--- Order menu ---")
            print("1. Create new order")
            print("2. Read order details")
            print("3. Update order details")
            print("4. Delete order")
            print("5. Go back")
            choice = input("\nEnter your choice: ")

            if choice == "1":
                customer_id = int(input("\nEnter customer ID: "))
                order_date = input("Enter order date: ")
                
                order_id = self.order_factory.create_order(customer_id, order_date)
                print("\nOrder created with ID: ", order_id)
            elif choice == "2":
                order_id = int(input("\nEnter order ID: "))
                order = self.order_factory.get_order(order_id)
                if order:
                    print("ID: ", order['id'])
                    print("Customer ID: ", order['customer_id'])
                    print("Order Date: ", order['order_date'])
                    
                else:
                    print("Order not found!")
            elif choice == "3":
                order_id = int(input("\nEnter order ID: "))
                order = self.order_factory.get_order(order_id)
                if order:
                    customer_id = input("Enter new customer ID : ")
                    customer_id = customer_id or order['customer_id']
                    order_date = input("Enter new order date : ")
                    order_date = order_date or order['order_date']
                      
                    self.order_factory.update_order(order_id, customer_id, order_date)
                    print("Order updated successfully!")
                else:
                    print("Order not found!")
            elif choice == "4":
                order_id = int(input("\nEnter order ID: "))
                if self.order_factory.delete_order(order_id):
                    print("Order deleted successfully!")
                else:
                    print("Order not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")     




    def order_item_menu(self):
        while True:
            print("\n--- Order Item menu ---")
            print("1. Create new order item")
            print("2. Read order item details")
            print("3. Update order item details")
            print("4. Delete order item")
            print("5. Go back")
            choice = input("Enter your choice: ")

            if choice == "1":
                order_id = int(input("\nEnter order ID: "))
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))
                self.order_item_factory.create_order_item(order_id, product_id, quantity)
                print("Order item created successfully!")
            elif choice == "2":
                order_item_id = int(input("\nEnter order item ID: "))
                order_item = self.order_item_factory.read_order_item(order_item_id)
                if order_item:
                    print("ID: ", order_item[0])
                    print("Order ID: ", order_item[1])
                    print("Product ID: ", order_item[2])
                    print("Quantity: ", order_item[3])
                else:
                    print("Order item not found!")
            elif choice == "3":
                order_item_id = int(input("\nEnter order item ID: "))
                order_item = self.order_item_factory.read_order_item(order_item_id)
                if order_item:
                    order_id = input("Enter new order ID : ")
                    product_id = input("Enter new product ID : ")
                    quantity = input("Enter new quantity : ")
                    self.order_item_factory.update_order_item(order_item_id, order_id, product_id, quantity)
                    print("Order item updated successfully!")
                else:
                    print("Order item not found!")
            elif choice == "4":
                order_item_id = int(input("\nEnter order item ID: "))
                if self.order_item_factory.delete_order_item(order_item_id):
                    print("\nOrder item deleted successfully!")
                else:
                    print("Order item not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")                            



    def transaction_menu(self):
        while True:
            print("\n--- Transaction menu ---")
            print("1. Create new transaction")
            print("2. Read transaction details")
            print("3. Update transaction details")
            print("4. Delete transaction")
            print("5. Go back")
            choice = input("Enter your choice: ")
        
            if choice == "1":
                customer_id = int(input("\nEnter customer ID: "))
                transaction_date = input("Enter transaction date (yyyy-mm-dd): ")
                credit_points = float(input("Enter credit points: "))
                self.transaction_factory.create_transaction(customer_id, transaction_date, credit_points)
                print("Transaction created successfully!")
            elif choice == "2":
                transaction_id = int(input("\nEnter transaction ID: "))
                transaction = self.transaction_factory.read_transaction(transaction_id)
                if transaction:
                    print("ID: ", transaction[0])
                    print("Order ID: ", transaction[1])
                    print("Transaction Date: ", transaction[2])
                    print("Amount: ", transaction[3])
                else:
                    print("Transaction not found!")
            elif choice == "3":
                transaction_id = int(input("\nEnter transaction ID: "))
                transaction = self.transaction_factory.read_transaction(transaction_id)
                if transaction:
                    customer_id = input("Enter new customer ID : ")
                    transaction_date = input("Enter new transaction date : ")
                    credit_points = input("Enter new credit points : ")
                    self.transaction_factory.update_transaction(transaction_id, customer_id, transaction_date, credit_points)
                    print("\nTransaction updated successfully!")
                else:
                    print("Transaction not found!")
            elif choice == "4":
                transaction_id = int(input("\nEnter transaction ID: "))
                if self.transaction_factory.delete_transaction(transaction_id):
                    print("\nTransaction deleted successfully!")
                else:
                    print("Transaction not found!")
            elif choice == "5":
                break
            else:
                print("Invalid choice!")
    