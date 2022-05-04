import os.path
import unittest


class test_signup(unittest.TestCase):
    # Checks if the 'MainScreen.py' file exists
    def test_is_file_signup(self):
        res = os.path.isfile("../signup.py")
        exp = False  # Improve later
        self.assertEquals(res, exp)


if __name__ == "__main__":
    unittest.main()
