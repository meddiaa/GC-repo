import mysql.connector
from mysql.connector import Error

def connect_to_DB():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="oussama",
            password="projet2cp",
            database="projet2cp",
            port="3306"
        )
        cursor = connection.cursor()
        return connection, cursor
    except Error as e:
        print(f"Erreur lors de la connexion à la base de données: {e}")
        return None, None