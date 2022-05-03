import os.path
from unicodedata import name 
from urllib import response
import requests
import json


# Checks if the 'login.py' file exists
def test_is_file_login():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\login.py"))

# needs a url
def main_url():
    return ""

# need status code and token
def test_login_valid():
    url = 
    data = { 'email': '' , 'password': ''}
    response = requests.post(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 
    
    
def main():
    test_is_file_login()
    main_url()
    test_login_valid()

if __name__ =='__main__':
    main()