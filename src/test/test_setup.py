import os.path
import unittest


class test_setup(unittest.TestCase):
    # Checks if the 'MainScreen.py' file exists
    def test_is_file_setup(self):
        res = os.path.isfile("setup.py")
        exp = True  # Improve later
        self.assertEquals(res, exp)


if __name__ == "__main__":
    unittest.main()
