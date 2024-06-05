# Main - Hlavní třída pro inicializaci a spuštění aplikace.


from db_connect import DbConnection
from ui import UI

class Main:
    """
    Třída Main je zodpovědná za inicializaci připojení k databázi a spuštění uživatelského rozhraní.
    
    Metody:
    - main(): Statická metoda, která inicializuje připojení k databázi, ověří připojení a spustí uživatelské rozhraní.
    """
    
    @staticmethod
    def main():
        # Inicializace připojení k databázi
        db_conn = DbConnection.get_instance()
        connection = db_conn.connection
        cursor = connection.cursor()

        # Ověření připojení k databázi
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        print("Connected to database: ", result)

        # Inicializace a spuštění uživatelského rozhraní
        ui = UI()
        ui.menu()

    if __name__ == "__main__":
        main()
