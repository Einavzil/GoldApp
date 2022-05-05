import unittest
import sys

sys.path.insert(0, "..\src")

from Registration.Registration import Ui_MainWindow


class test_main(unittest.TestCase):
    def test_init(self):
        res = Ui_MainWindow()
        exp = Ui_MainWindow
        self.assertIsInstance(res, exp)


if __name__ == "__main__":
    unittest.main()
