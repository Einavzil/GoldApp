import os.path

# Tests if  the 'registratition.py' file exists
def test_is_file_registration():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\Registration\Registration.py"
        )
    )


def main():
    test_is_file_registration()


if __name__ == "__main__":
    main()
