import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@123",
        database="hotel_db"
    )
