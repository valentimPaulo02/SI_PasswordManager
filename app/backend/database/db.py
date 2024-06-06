import mysql.connector, os
from mysql.connector import errorcode

def make_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',         # -------------------------- ENV VARIABLE
            user='root',              # -------------------------- ENV VARIABLE
            password='paulinhomysql', # -------------------------- ENV VARIABLE
            database='password_manager' 
        )
        return conn
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return None