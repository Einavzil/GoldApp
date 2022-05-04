import os.path


# Checks if the 'card_widget.py' file exists
def test_is_file_card_widget():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\card_widget.py"
        )
    )


def main():
    test_is_file_card_widget()


if __name__ == "__main__":
    main()
