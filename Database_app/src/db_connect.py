from mysql.connector import Error
from mysql.connector import MySQLConnection
from configparser import ConfigParser
import os
class DbConnection:
    __instance = None

    @staticmethod 
    def get_instance():
        """ Static access method. """
        if DbConnection.__instance == None:
            DbConnection()
        return DbConnection.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DbConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            DbConnection.__instance = self
            self.connection = self.connect()

    def read_db_config(self, filename='config/config.ini', section='mysql'):
        """Read database configuration file and return a dictionary object"""
        try:
            # Create parser and read ini configuration file
            parser = ConfigParser()
            script_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(script_dir, '..', filename)
            parser.read(file_path)

            # Get section, default to mysql
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
        """ Connect to the database. """
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
        try:
            if not hasattr(self, 'connection'):
                self.connection = self.connect()
            return self.connection.cursor()
        except Error as error:
            print("Error creating cursor:", error)

       