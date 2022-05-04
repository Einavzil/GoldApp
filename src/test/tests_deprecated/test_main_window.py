import os.path


# Checks if the 'main_screen.py' file exists
def test_is_file_main_window():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\main_window.py"
        )
    )


def main():
    test_is_file_main_window()


if __name__ == "__main__":
    main()
