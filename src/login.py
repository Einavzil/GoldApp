import mysql.connector

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
            if result[0] == password:
                return True
            return False

    except Exception as err:
        print(err)
        

if __name__ == "__main__":
    print(check_email('example@gmail.com'))
    if check_email('example@gmail.com'):
        print(check_password('example@gmail.com', 'abc123'))

