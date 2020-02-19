#!/usr/bin/python3
"""Unit tests for BaseModel"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime as dt
import os


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

    def test_attributes_BaseModel(self):
        """Tests for attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """Tests if BaseTest is a type BaseModel"""
        self.assertTrue(isinstance(self.BaseTest, BaseModel))
        self.assertEqual(self.BaseTest.name, "Mike")
        self.assertEqual(self.BaseTest.number, 55)

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

    def test_save_BaseModel(self):
        """Tests if saving works"""
        self.BaseTest.save()
        self.assertNotEqual(self.BaseTest.created_at, self.BaseTest.updated_at)

    def test_create_BaseModel(self):
        """tests if it can create a base model"""
        base = self.BaseTest
        now = dt.now()
        self.assertIsInstance(base.created_at, dt)
        self.assertTrue(now >= base.created_at)

    def test_update_BaseModel(self):
        """Tests the update function"""
        base = self.BaseTest
        base.updated_at = dt.now()
        store = base.updated_at
        self.assertIsInstance(base.updated_at, dt)
        base.updated_at = dt.now()
        self.assertNotEqual(base.updated_at, store)

    def test_str_BaseModel(self):
        """Tests the string"""
        string = "[BaseModel] ({}) {}".format(self.BaseTest.id,
                                              self.BaseTest.__dict__)
        self.assertEqual(string, str(self.BaseTest))

if __name__ == "__main__":
    unittest.main()
