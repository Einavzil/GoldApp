import os.path
import unittest


class test_setup(unittest.TestCase):
    """Unit test for setup.py file."""

    def test_is_file_setup(self):
        """Checks if the 'setup.py' file exists."""
        res = os.path.isfile("src\setup.py")
        exp = True
        self.assertEqual(res, exp)
        

if __name__ == "__main__":
    unittest.main()
