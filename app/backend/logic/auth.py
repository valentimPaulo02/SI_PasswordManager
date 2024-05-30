import mysql.connector
from backend.database.db import *
from backend.security.hash import *

def manage_user(username, password, scd_password, new):
    if(password!=scd_password):
        print("Passwords dont match.")
        return False

    conn = make_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    try:
        if(new):
            cursor.execute('''
            INSERT INTO users (username, password) VALUES (%s, %s)
            ''', (username, hashed_password))
            conn.commit()
        else:
            cursor.execute('''
            UPDATE users SET password = %s WHERE username = %s
            ''', (hashed_password, username))
            conn.commit()
        return True
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    
    finally:
        conn.close()


def login_user(username, password):
    conn = make_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT password, user_id FROM users WHERE username = %s
    ''', (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result and check_password(result[0], password):
        return result[1]
    else:
        return -1
    

def update_password(username, password, scd_password):
    conn = make_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM users WHERE username = %s
    ''', (username,))
    result = cursor.fetchone()
    
    conn.close()

    if(result == None):
        print("Username doesnt exist.")
        return False

    if(manage_user(username, password, scd_password, False)):
        return True
    else:
        return False 