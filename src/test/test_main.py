# flake8: noqa
import os.path
from unicodedata import name


def main():
    test_is_file_main()


# Checks if the 'Main.py' file file exists
def test_is_file_main():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\main.py"))


if __name__ == "__main__":
    main()
