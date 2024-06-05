from mysql.connector import Error
from mysql.connector import MySQLConnection
from configparser import ConfigParser
import os
class DbConnection:
    __instance = None

    @staticmethod 
    def get_instance():
        """
        Statická metoda pro přístup k instanci DbConnection.
        Pokud instance ještě neexistuje, vytvoří ji.
        """

        if DbConnection.__instance == None:
            DbConnection()
        return DbConnection.__instance

    def __init__(self):
        """
        Prakticky privátní konstruktor.
        Zajišťuje, že je vytvořena pouze jedna instance třídy.
        """
        if DbConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DbConnection.__instance = self
            self.connection = self.connect()

    def read_db_config(self, filename='config/config.ini', section='mysql'):
        """
        Přečte konfigurační soubor databáze a vrátí slovník s konfigurací.
        filename: Název konfiguračního souboru (default: 'config/config.ini')
        section: Sekce v konfiguračním souboru, která obsahuje nastavení databáze (default: 'mysql')
        """
        try:
            # Vytvoření parseru a přečtení ini konfiguračního souboru
            parser = ConfigParser()
            script_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(script_dir, '..', filename)
            parser.read(file_path)

            # Získání sekce, defaultně nastaveno na mysql
            db = {}
            if parser.has_section(section):
                items = parser.items(section)
                for item in items:
                    db[item[0]] = item[1]
            else:
                raise Exception('{0} not found in the {1} file'.format(section, filename))

            return db
        except Exception as error:
            print("Error reading database configuration file:", error)

    def connect(self):
        """
        Připojení k databázi MySQL.
        Načte konfiguraci z konfiguračního souboru a vytvoří spojení s databází.
        """
        db_config =  self.read_db_config()
        try:
            print("Connecting to MySQL database...")
            conn = MySQLConnection(**db_config)

            if conn.is_connected():
                print("Connection established.")
                return conn
            else:  
                raise Exception("Connection failed.")

        except Error as error:
            print("Error connecting to MySQL database:", error)

    def cursor(self):
        """
        Vytvoří a vrátí kurzor pro provádění databázových operací.
        Pokud spojení ještě neexistuje, vytvoří ho.
        """
        try:
            if not hasattr(self, 'connection'):
                self.connection = self.connect()
            return self.connection.cursor()
        except Error as error:
            print("Error creating cursor:", error)

       