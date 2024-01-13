#!/usr/bin/python3
"""
    Module to implement test cases for the
    User class

"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class User test cases"""
    def setUp(self):
        """Prepares environment for each test case"""
        self.user = User()

    def tearDown(self):
        """Clears environment after each test case"""
        self.user = None

    def test_email_attribute(self):
        """Test email attribute"""
        email = "user@example.com"
        self.user.email = email
        self.assertEqual(self.user.email, email)

    def test_password_attribute(self):
        """Test password attribute"""
        pswd = "secure@12wordpass"
        self.user.pswd = pswd
        self.assertEqual(self.user.pswd, pswd)

    def test_first_name_attribute(self):
        """Test first name attribute"""
        first_name = "Jude"
        self.user.first_name = first_name
        self.assertEqual(self.user.first_name, first_name)

    def test_last_name_attribute(self):
        """Test user last name attribute"""
        last_name = "Lawan"
        self.user.last_name = last_name
        self.assertEqual(self.user.last_name, last_name)


if __name__ == "__main__":
    unittest.main()
