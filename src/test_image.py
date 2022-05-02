import mysql.connector
import urllib.request 
from PIL import Image


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
        
def retrive_image():
    conn, cursor = connect()
    sql = """
    SELECT image_path
    FROM interest
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    print(result)
    urllib.request.urlretrieve(result[0], 'cooking')
    img = Image.open('cooking')
    img.show()
    
if __name__ == "__main__":
    retrive_image()