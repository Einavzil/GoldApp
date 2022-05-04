import os.path


# Checks if the 'new_account_window.py' file exists
def test_is_file_new_account_window():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\new_account_window.py"
        )
    )


def main():
    test_is_file_new_account_window()


if __name__ == "__main__":
    main()
