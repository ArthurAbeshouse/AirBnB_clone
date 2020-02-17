#!/usr/bin/python3
"""Unit tests for city"""
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City


class TestConsole(unittest.TestCase):
    """Tests for City class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.CityTest = City()
        cls.CityTest.name = "NH"
        cls.CityTest.state_id = "CT"

    @classmethod
    def tearDown(cls):
        """Tears down testing methods"""
        del cls.CityTest
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_City(self):
        """Tests docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Tests for attributes"""
        self.assertTrue('id' in self.CityTest.__dict__)
        self.assertTrue('created_at' in self.CityTest.__dict__)
        self.assertTrue('updated_at' in self.CityTest.__dict__)
        self.assertTrue('state_id' in self.CityTest.__dict__)
        self.assertTrue('name' in self.CityTest.__dict__)

    def test_subclass_City(self):
        """Tests if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.CityTest.__class__, BaseModel), True)
        self.assertIsInstance(self.CityTest, City)

    def test_attribute_types_City(self):
        """Tests the attributes of City"""
        self.assertEqual(type(self.CityTest.name), str)
        self.assertEqual(type(self.CityTest.state_id), str)

    def test_save_City(self):
        """Tests if saving works"""
        self.CityTest.save()
        self.assertNotEqual(self.CityTest.created_at, self.CityTest.updated_at)

    def test_to_dict_City(self):
        """Tests if dictionary is functional"""
        self.assertEqual('to_dict' in dir(self.CityTest), True)


if __name__ == "__main__":
    unittest.main()
