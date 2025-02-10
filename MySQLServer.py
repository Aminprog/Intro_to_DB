import mysql.connector
from mysql.connector import Error

def create_database():
    """Function to create the database alx_book_store in MySQL Server."""
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host="0.0.0.0",
            user="root",  # Replace with your MySQL username
            password="your_new_password"  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Catch only MySQL errors
        print(f"Error connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

