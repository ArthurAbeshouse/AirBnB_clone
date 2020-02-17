#!/usr/bin/python3
"""Unit tests for user"""
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Tests for User class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.UserTest = User()
        cls.UserTest.first_name = "Betty"
        cls.UserTest.last_name = "Holberton"
        cls.UserTest.email = "BettyHolberton@holbertonschool.com"
        cls.UserTest.password = "qwerty"

    @classmethod
    def tearDown(cls):
        """Tears down testing methods"""
        del cls.UserTest
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_User(self):
        """Tests docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """Tests for attributes"""
        self.assertTrue('email' in self.UserTest.__dict__)
        self.assertTrue('id' in self.UserTest.__dict__)
        self.assertTrue('created_at' in self.UserTest.__dict__)
        self.assertTrue('updated_at' in self.UserTest.__dict__)
        self.assertTrue('password' in self.UserTest.__dict__)
        self.assertTrue('first_name' in self.UserTest.__dict__)
        self.assertTrue('last_name' in self.UserTest.__dict__)

    def test_subclass_User(self):
        """Tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.UserTest.__class__, BaseModel), True)
        self.assertIsInstance(self.UserTest, User)

    def test_attribute_types_User(self):
        """Tests the attributes of User"""
        self.assertEqual(type(self.UserTest.first_name), str)
        self.assertEqual(type(self.UserTest.last_name), str)
        self.assertEqual(type(self.UserTest.email), str)
        self.assertEqual(type(self.UserTest.password), str)
        self.assertNotEqual(hasattr(self.UserTest, "name"), True)

    def test_save_User(self):
        """Tests if saving works"""
        self.UserTest.save()
        self.assertNotEqual(self.UserTest.created_at, self.UserTest.updated_at)

    def test_to_dict_User(self):
        """Tests if dictionary is functional"""
        self.assertEqual('to_dict' in dir(self.UserTest), True)


if __name__ == "__main__":
    unittest.main()
