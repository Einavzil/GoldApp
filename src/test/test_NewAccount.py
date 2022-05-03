import os.path

# Checks if the 'NewAccount.py' file exists
def test_is_file_NewAccount():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\NewAccount\NewAccount.py"
        )
    )


def main():
    test_is_file_NewAccount()


if __name__ == "__main__":
    main()
