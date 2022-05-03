import os.path


# Checks if the 'signup.py' file exists
def test_is_file_signup():
    print(os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\signup.py"))

def main():
    test_is_file_signup()


if __name__ == "__main__":
    main()
