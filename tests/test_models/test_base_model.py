#!/usr/bin/python3
"""Unit tests for BaseModel"""
import os
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime as dt
import pep8


class TestBaseModel(unittest.TestCase):
    """Tests for basemodel class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.BaseTest = BaseModel()
        cls.BaseTest.name = "Mike"
        cls.BaseTest.number = 55

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_attributes_BaseModel(self):
        """Tests for attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Tests if BaseTest is a type BaseModel"""
        self.assertTrue(isinstance(self.BaseTest, BaseModel))

    def test_to_dict_BaseModel(self):
        """Tests if dictionary is functional"""
        B_Dict = self.BaseTest.to_dict()
        self.assertEqual(self.BaseTest.__class__.__name__, 'BaseModel')
        self.assertEqual(B_Dict["__class__"], 'BaseModel')
        self.assertIsInstance(B_Dict['created_at'], str)
        self.assertIsInstance(B_Dict['updated_at'], str)

    def test_id_BaseModel(self):
        """Tests for unique ids"""
        self.assertIsInstance(self.BaseTest.id, str)
        self.assertIsInstance(uuid.UUID(self.BaseTest.id), uuid.UUID)

    def test_create_BaseModel(self):
        """tests if it can create a base model"""
        base = self.BaseTest
        base.created_at = dt.now()
        self.assertIsInstance(base.created_at, dt)

    def Test_kwargs_BaseModel(self):
        """Tests **kwargs"""
        base_model = self.BaseTest
        base_model.name = self.BaseTest.name
        base_model.number = self.BaseTest.number
        base_model_json = base_model.to_dict()
        new_base_model = self.BaseTest(**base_model_json)
        self.assertEqual(new_base_model.to_dict(), base_model.to_dict())

    def test_update_BaseModel(self):
        """Tests the update function"""
        base = self.BaseTest
        base.updated_at = dt.now()
        store = base.updated_at
        self.assertIsInstance(base.updated_at, dt)
        base.updated_at = dt.now()
        self.assertNotEqual(base.updated_at, store)

if __name__ == "__main__":
    unittest.main()
