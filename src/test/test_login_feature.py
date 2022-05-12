import unittest
import sys, os
import mysql.connector
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import login


class test_login(unittest.TestCase):
    """Unit tests for login.py file."""
    
    def test_is_file_login(self):
        """Checks if the 'login.py' file exists."""
        res = os.path.isfile("src\login.py")
        exp = True
        self.assertEqual(res, exp)    
    
    # def test_run_main(self):
        
        
   

if __name__ == "__main__":
    unittest.main()
