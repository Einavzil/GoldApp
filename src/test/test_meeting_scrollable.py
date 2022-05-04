import os.path


# Checks if the 'meeting_scrollable.py' file exists
def test_is_file_meeting_scrollable():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\meeting_scrollable.py"
        )
    )


def main():
    test_is_file_meeting_scrollable()


if __name__ == "__main__":
    main()
