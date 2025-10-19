import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust user and password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword"  # <-- Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close database connection properly
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
