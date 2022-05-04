import os.path
import unittest


class test_is_NewAccount(unittest.TestCase):
    # Checks if the 'NewAccount.py' file exists
    def test_is_file_NewAccount(self):
        res = os.path.isdir("../NewAccount")
        exp = False
        self.assertAlmostEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
