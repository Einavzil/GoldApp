import os.path
import unittest


class test_registration(unittest.TestCase):
    # Checks if the 'MainScreen.py' file exists
    def test_is_file_registration(self):
        res = os.path.isfile("registration.py")
        exp = False  # Improve later
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
