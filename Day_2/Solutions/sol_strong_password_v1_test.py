import unittest
import Day_2.Solutions.sol_strong_password_v1 as sspv1


class TestStrongPassword(unittest.TestCase):
    def test_digits(self):
        """ Test only digits """
        status, msg = sspv1.check_password("ppU!GNnu")
        self.assertFalse(status) # check that value status is False
        self.assertIsInstance(msg, str)
        self.assertRegex(msg, 'digits not in password')
        
    def test_wrong_symbol(self):
        self.assertRaises(ValueError, sspv1.check_password, "1pUц2Gn*")    
        with self.assertRaises(ValueError) as te:
            sspv1.check_password("1pUц2Gn*")
        exception = te.exception
        self.assertIsInstance(exception, ValueError)
        self.assertRegex(str(exception), "wrong char in password")

    def test_uppercase(self):
        status, msg = sspv1.check_password("ppU!GNn1".lower())
        self.assertFalse(status)
        self.assertIsInstance(msg, str)
        self.assertRegex(msg, 'uppercase not in password')
        
    def test_lowercase(self):
        status, msg = sspv1.check_password("ppU!GNn1".upper())
        self.assertFalse(status)
        self.assertIsInstance(msg, str)
        self.assertRegex(msg, 'lowercase not in password')
        
    def test_special(self):
        status, msg = sspv1.check_password("ppUgGNn1")
        self.assertFalse(status)
        self.assertIsInstance(msg, str)
        self.assertRegex(msg, 'special not in password')
    
    def test_correct_passwords(self):
        password = 'ppU!GNn'
        for i in range(0, 8):
            password += str(i)
            status, msg = sspv1.check_password(password)
            self.assertTrue(status)
            self.assertIsInstance(msg, str)
            self.assertEqual(len(msg), 0)
    
    def test_len(self):
        """ check min and max lengths errors """
        for pswd in ("ppUgGNn", "ppUgGNn1ppUgGNn1"):
            status, msg = sspv1.check_password(pswd)
            self.assertFalse(status)
            self.assertIsInstance(msg, str)
            self.assertRegex(msg, 'password (low|high) len')
            


if __name__ == "__main__":
    unittest.main(verbosity=2)