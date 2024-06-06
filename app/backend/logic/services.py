import mysql.connector
from backend.database.db import *
from backend.security.encrypt import *
from backend.security.password import *

def create_service(user_id, service, username, password):
    conn = make_connection()
    cursor = conn.cursor()

    if(password == ""): password = generate_password()

    encrypted_password = encrypt_password(password) 

    try:
        cursor.execute('''
        INSERT INTO accounts (user_id, service, username, password) VALUES (%s, %s, %s, %s)
        ''', (user_id, service, username, encrypted_password))
        conn.commit()
        return True
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    
    finally:
        conn.close()


def get_services(user_id):
    conn = make_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT service, username, password FROM accounts WHERE user_id = %s
    ''', (user_id,))
    result = cursor.fetchall()
    
    conn.close()

    return result


def update_password(password, user_id, service):
    conn = make_connection()
    cursor = conn.cursor()
    
    encrypted_password = encrypt_password(password) 

    try:
        cursor.execute('''
        UPDATE accounts SET password = %s WHERE user_id = %s AND service = %s
        ''', (encrypted_password, user_id, service))
        conn.commit()
        return True
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    
    finally:
        conn.close()
    