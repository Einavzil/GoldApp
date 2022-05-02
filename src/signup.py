import mysql.connector
from cryptography.fernet import Fernet

def connect():
    dsn = {
        "user": "maria",
        "password": "password",
        "host": "127.0.0.1",
        "port": "3306",
        "database": "goldapp",
        "raise_on_warnings": True,
        }
    try:
        conn =  mysql.connector.connect(**dsn)
        cursor = conn.cursor(prepared=True)
        return conn, cursor
    except Exception as err:
        print(err)
        
def insert_account(fname, lname, email, pwd, phone, location):
    conn, cursor = connect()
    enc_pwd = encrypt_pass(pwd)
    
    sql = """
    INSERT INTO user (email, fname, lname, pwd, phone)
    VALUES (?, ?, ?, ?, ?)
    ;
    """
    args = (email, fname, lname, enc_pwd, phone)
    cursor.execute(sql, args)
    conn.commit()
    
    sql_id_statement = """
    SELECT LAST_INSERT_ID()
    FROM user
    ;
    """
    
    cursor.execute(sql_id_statement)
    user_id = cursor.fetchone()

    
    return email
    
def encrypt_pass(pwd):
    with open('src/enc_key.bin', 'rb') as key_file:
        key = key_file.readline()
    
    fernet = Fernet(key)
    enc_pwd = fernet.encrypt(pwd.encode())
    
    return enc_pwd.decode()

def add_interest(user_id, interest):
    
    conn, cursor = connect()
    sql = """
    INSERT INTO user_has_interest (interest_interest_id, user_email)
    VALUES (?, ?)
    ;
    """
    
    cursor.execute(sql, (interest, user_id))
    print(cursor.fetchone())
    conn.commit()
    
    cursor.close()
    conn.close()
