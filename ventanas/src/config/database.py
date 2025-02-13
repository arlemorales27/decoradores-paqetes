import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='mi_db',
                user='root',
                password=''
            )
        except Error as e:
            print(f"Error conectando a MySQL: {e}")

    def get_connection(self):
        return self.connection
