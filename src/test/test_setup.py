import os.path


# Checks if the 'setup.py' file exists
def test_is_file_setup():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\setup.py"))


def main():
    test_is_file_setup()


if __name__ == "__main__":
    main()
