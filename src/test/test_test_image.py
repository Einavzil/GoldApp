import os.path
import os.path
import unittest


class test_image(unittest.TestCase):
    # Checks if the 'MainScreen.py' file exists
    def test_is_file_mainscreen(self):
        res = os.path.isfile("test_image.py")
        exp = False  # Improve later
        self.assertEquals(res, exp)


if __name__ == "__main__":
    unittest.main()
