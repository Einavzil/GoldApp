import mysql.connector
from cryptography.fernet import Fernet

def check_email(email):
    try:
        dsn = {
        "user": "maria",
        "password": "password",
        "host": "127.0.0.1",
        "port": "3306",
        "database": "goldapp",
        "raise_on_warnings": True,
    }
        with mysql.connector.connect(**dsn) as conn:
            cursor = conn.cursor(prepared=True)
                
            sql = """
                SELECT
                email
                FROM user
                WHERE email = ?
                ;
                """
            args = (email,)
            cursor.execute(sql, args)
            result = cursor.fetchone()
            if result[0] == email:
                return True
            
        return False
    
    except Exception as err:
        print(err)

def check_password(email, password):
    try:
        dsn = {
        "user": "maria",
        "password": "password",
        "host": "127.0.0.1",
        "port": "3306",
        "database": "goldapp",
        "raise_on_warnings": True,
    }
        with mysql.connector.connect(**dsn) as conn:
            cursor = conn.cursor(prepared=True)
            sql = """
                SELECT
                pwd
                FROM user
                WHERE email = ?
                ;
                """

            args = (email,)
            cursor.execute(sql, args)
            result = cursor.fetchone()
            decrepted_pass = decrypt_pass(result[0])
            if decrepted_pass == password:
                return True
            return False

    except Exception as err:
        print(err)

def encrypt_pass(password):
    with open('enc_key.bin', 'rb') as key_file:
        key = key_file.readline()
    
    fernet = Fernet(key)
    enc_pass = fernet.encrypt(password.decode())
    
    # code be added here when creating an account to store encrypted password in the database
    
def decrypt_pass(password):
    """Key is opened from 'enc_key.bin' file."""

    with open('enc_key.bin', 'rb') as key_file:
        key = key_file.readline()

    fernet = Fernet(key)
    """decrypting the password into string and return it."""
    decr_pass = fernet.decrypt(password.encode())

    return decr_pass.decode()

if __name__ == "__main__":
    print(check_email('example@gmail.com'))
    if check_email('example@gmail.com'):
        print(check_password('example@gmail.com', 'abc123'))

