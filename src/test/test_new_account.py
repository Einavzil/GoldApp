import unittest
import sys

sys.path.insert(0, "../src")

from NewAccount.NewAccount import Ui_Form


class test_main(unittest.TestCase):
    def test_init(self):
        res = Ui_Form()
        exp = Ui_Form
        self.assertIsInstance(res, exp)


if __name__ == "__main__":
    unittest.main()
