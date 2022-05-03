import os.path

# Checks if the 'MainScreen.py' file exists
def test_is_file_mainscreen():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\MainScreen\MainScreen.py"
        )
    )


def main():
    test_is_file_mainscreen()


if __name__ == "__main__":
    main()
