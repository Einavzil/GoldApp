# flake8: noqa
import os.path
from unicodedata import name


def main():
    test_is_file_main()
    test_is_file_mainscreen()
    test_is_file_login()
    test_is_file_setup()
    test_is_file_signup()
    test_is_file_test_image()


# Checks if the 'Main.py' file file exists
def test_is_file_main():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\main.py"))


# Checks if the 'MainScreen.py' file exists
def test_is_file_mainscreen():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\MainScreen\MainScreen.py"
        )
    )


# Checks if the 'login.py' file exists
def test_is_file_login():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\login.py"))


# Checks if the 'setup.py' file exists
def test_is_file_setup():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\setup.py"))


# Checks if the 'signup.py' file exists
def test_is_file_signup():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\signup.py"))


# Checks if the 'test_image.py' file exists
def test_is_file_test_image():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\test_image.py"))


if __name__ == "__main__":
    main()
