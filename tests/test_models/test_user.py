#!/usr/bin/python3
"""Unit tests for user"""
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
import uuid
from datetime import datetime as dt


class TestUser(TestBaseModel):
    """Tests for User class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.UserTest = User()
        cls.UserTest.first_name = "Betty"
        cls.UserTest.last_name = "Holberton"
        cls.UserTest.email = "BettyHolberton@holbertonschool.com"
        cls.UserTest.password = "qwerty"

    def test_subclass_User(self):
        """Tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.UserTest.__class__, BaseModel), True)
        self.assertIsInstance(self.UserTest, User)

    def test_attribute_types_User(self):
        """Tests the attributes of User"""
        self.assertIsNotNone(self.UserTest.first_name)
        self.assertIsNotNone(self.UserTest.last_name)
        self.assertIsNotNone(self.UserTest.email)
        self.assertIsNotNone(self.UserTest.password)
        self.assertEqual(type(self.UserTest.first_name), str)
        self.assertEqual(type(self.UserTest.last_name), str)
        self.assertEqual(type(self.UserTest.email), str)
        self.assertEqual(type(self.UserTest.password), str)
        self.assertNotEqual(hasattr(self.UserTest, "name"), True)

    def test_save_User(self):
        """Tests if saving works"""
        self.UserTest.save()
        self.assertNotEqual(self.UserTest.created_at, self.UserTest.updated_at)

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass
