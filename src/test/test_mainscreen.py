import os.path
import unittest


class test_mainscreen(unittest.TestCase):
    # Checks if the 'MainScreen.py' file exists
    def test_is_file_mainscreen(self):
        res = os.path.isfile("MainScreen.py")
        exp = False
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
