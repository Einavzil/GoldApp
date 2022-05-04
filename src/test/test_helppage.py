import os.path


# Checks if the 'Helppage.py' file exists
def test_is_file_helppage():
    print(
        os.path.exists(r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\HelpPage.py")
    )


def main():
    test_is_file_helppage()


if __name__ == "__main__":
    main()
