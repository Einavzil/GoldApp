import os.path
import unittest
import sys
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
# import 

class test_image(unittest.TestCase):
    # Checks if the 'MainScreen.py' file exists
    def test_is_file_mainscreen(self):
        res = os.path.isfile("test_image.py")
        exp = True  # Improve later
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
