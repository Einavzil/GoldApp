import os.path


# Checks if the 'mainwindowtwo.py' file exists
def test_is_file_mainwindowtwo():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\mainwindowtwo.py"
        )
    )


def main():
    test_is_file_mainwindowtwo()


if __name__ == "__main__":
    main()
