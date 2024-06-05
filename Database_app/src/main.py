from db_connect import DbConnection
from ui import UI

class Main:
    @staticmethod
    def main():
        db_conn = DbConnection.get_instance()
        connection = db_conn.connection
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        print("Connected to database: ", result)
        ui = UI()
        ui.menu()

    if __name__ == "__main__":
        main()
        