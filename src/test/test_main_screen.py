import os.path


# Checks if the 'main_screen.py' file exists
def test_is_file_main_screen():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\main_screen.py"
        )
    )


def main():
    test_is_file_main_screen()


if __name__ == "__main__":
    main()
