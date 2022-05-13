import unittest
import sys, os
import mysql.connector, datetime
sys.path.append(os.path.abspath(os.getcwd()) + "/src/")
import daily_survey_db


class test_daily_survey_db(unittest.TestCase):
    """Unit tests for daily_survey_db.py file."""
    
    def test_is_file_daily_survey_db(self):
        """Checks if the 'daily_survey_db.py' file exists."""
        res = os.path.isfile("src\daily_survey_db.py")
        exp = True
        self.assertEqual(res, exp)

   
    def test_connect(self):
        """Test the connection."""
        conn, cursor = daily_survey_db.connect()
        res = conn
        exp = mysql.connector.connection_cext.CMySQLConnection
        self.assertIsInstance(res, exp)
        
        res = cursor
        exp = mysql.connector.cursor_cext.CMySQLCursorPrepared
        self.assertIsInstance(res, exp)
        

    def test_insert_data(self):
        """Test the insert data function with entering answers."""
        daily_survey_db.insert_data(1, 2, 3, "testing testing")
        conn, cursor = daily_survey_db.connect()
        sql = """
            select free_text
            from daily_survey
            ORDER BY daily_survey_id desc;
            ;
            """
        cursor.execute(sql,)
        result = cursor.fetchone()
        res = "testing testing"
        exp = result[0]
        self.assertEqual(res, exp)
    
    
    def test_check_last_survey(self):
        """Testing last survey if already done."""
        res = daily_survey_db.check_last_survey()
        conn, cursor = daily_survey_db.connect()
        with open("src/current_email.txt", "r") as email_file:
            email = email_file.readline()
        sql = """
        SELECT MAX(date), CURDATE()
        FROM daily_survey
        WHERE user_email = ?
        """
        args = (email,)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        if result[0] == None:
            self.assertIsNone(result[0])
        else:
            exp = False
            self.assertEqual(res, exp)            


if __name__ == "__main__":
    unittest.main()
