#!/usr/bin/python3
"""Unit tests for BaseModel"""
import os
import unittest
import pep8
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """Tests for basemodel class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.BaseTest = BaseModel()
        cls.BaseTest.phrase = "Drive"
        cls.BaseTest.number = 55

    @classmethod
    def tearDown(cls):
        """Tears down testing methods"""
        del cls.BaseTest
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_BaseModel(self):
        """Tests docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes_BaseModel(self):
        """Tests for attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Tests if BaseTest is a type BaseModel"""
        self.assertTrue(isinstance(self.BaseTest, BaseModel))

    def test_save_BaseModel(self):
        """Tests if saving works"""
        self.BaseTest.save()
        self.assertNotEqual(self.BaseTest.created_at, self.BaseTest.updated_at)

    def test_to_dict_BaseModel(self):
        """Tests if dictionary is functional"""
        B_Dict = self.BaseTest.to_dict()
        self.assertEqual(self.BaseTest.__class__.__name__, 'BaseModel')
        self.assertIsInstance(B_Dict['created_at'], str)
        self.assertIsInstance(B_Dict['updated_at'], str)

    def test_id_BaseModel(self):
        """Tests for unique ids"""
        ids = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(ids)), len(ids))

if __name__ == "__main__":
    unittest.main()
