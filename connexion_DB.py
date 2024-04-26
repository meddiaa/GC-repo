import mysql.connector
from mysql.connector import Error

def connect_to_DB():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="moh@med18082004",
            database="JSS",
            port="3306"
        )
        cursor = connection.cursor()
        return connection, cursor
    except Error as e:
        print(f"Erreur lors de la connexion à la base de données: {e}")
        return None, None
