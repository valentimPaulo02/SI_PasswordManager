import mysql.connector, os
from mysql.connector import errorcode

def make_connection():
    try:
        conn = mysql.connector.connect(
            host= #REPLACE WITH MYSQL DATABASE HOST - EXAMPLE: 'localhost'
            user= #REPLACE WITH MYSQL DATABASE USER - EXAMPLE: 'root'
            password= #REPLACE WITH MYSQL DATABASE PASSWORD - EXAMPLE: 'databasepassword'
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