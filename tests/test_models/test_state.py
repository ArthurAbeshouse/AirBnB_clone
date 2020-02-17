#!/usr/bin/python3
"""Unit tests for user"""
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.state import State


class TestConsole(unittest.TestCase):
    """Tests for State class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.StateTest = State()
        cls.StateTest.name = "CT"

    @classmethod
    def tearDown(cls):
        """Tears down testing methods"""
        del cls.StateTest
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_State(self):
        """Tests docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """Tests for attributes"""
        self.assertTrue('id' in self.StateTest.__dict__)
        self.assertTrue('created_at' in self.StateTest.__dict__)
        self.assertTrue('updated_at' in self.StateTest.__dict__)
        self.assertTrue('name' in self.StateTest.__dict__)

    def test_subclass_State(self):
        """Tests if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.StateTest.__class__, BaseModel), True)
        self.assertIsInstance(self.StateTest, State)

    def test_attribute_types_State(self):
        """Tests the attributes of State"""
        self.assertEqual(type(self.StateTest.name), str)
        self.assertEqual(hasattr(self.StateTest, "name"), True)

    def test_save_State(self):
        """Tests if saving works"""
        self.StateTest.save()
        self.assertNotEqual(self.StateTest.created_at, self.StateTest.updated_at)

    def test_to_dict_State(self):
        """Tests if dictionary is functional"""
        self.assertEqual('to_dict' in dir(self.StateTest), True)


if __name__ == "__main__":
    unittest.main()