import unittest
import sys, os
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
from Registration.Registration import Ui_MainWindow


class test_main(unittest.TestCase):
    """Unit tests for main.py file."""
    
    def test_init(self):
        """Window check."""
        res = Ui_MainWindow()
        exp = Ui_MainWindow
        self.assertIsInstance(res, exp)


    def test_is_file_main(self):
        """Checks if the 'main.py' file exists."""
        res = os.path.isfile("src\main.py")
        exp = True
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
