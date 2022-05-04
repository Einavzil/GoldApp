import os.path


# Checks if the 'meetings_events_all.py' file exists
def test_is_file_meetings_events_all():
    print(
        os.path.exists(
            r"C:\Users\rhyme\Documents\HKR\GoldApp\src\examples\meetings_events_all.py"
        )
    )


def main():
    test_is_file_meetings_events_all()


if __name__ == "__main__":
    main()
