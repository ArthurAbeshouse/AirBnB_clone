#!/usr/bin/python3
"""Unit tests for city"""
import os
import unittest
from models.base_model import BaseModel
from models.city import City
from tests.test_models.test_base_model import TestBaseModel
import uuid
from datetime import datetime as dt
import json
from models import storage


class TestCity(TestBaseModel):
    """Tests for City class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.CityTest = City()
        cls.CityTest.name = "NH"
        cls.CityTest.state_id = "CT"

#    def test_attributes_City(self):
#        """Tests for attributes"""
#        self.assertTrue('id' in self.CityTest.__dict__)
#        self.assertTrue('created_at' in self.CityTest.__dict__)
#        self.assertTrue('updated_at' in self.CityTest.__dict__)
#        self.assertTrue('state_id' in self.CityTest.__dict__)
#        self.assertTrue('name' in self.CityTest.__dict__)

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

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass
