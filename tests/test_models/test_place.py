#!/usr/bin/python3
"""Unit tests for Place"""
import os
import unittest
from models.base_model import BaseModel
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel
import uuid
from datetime import datetime as dt
from models import storage


class TestPlace(TestBaseModel):
    """Tests for Place class"""

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.PlaceTest = Place()
        cls.PlaceTest.city_id = "asdf-6789"
        cls.PlaceTest.user_id = "ghjl-1234"
        cls.PlaceTest.name = "Mohegan Sun"
        cls.PlaceTest.description = "a world at play"
        cls.PlaceTest.number_rooms = 1563
        cls.PlaceTest.number_bathrooms = 7
        cls.PlaceTest.max_guest = 96492
        cls.PlaceTest.price_by_night = 15
        cls.PlaceTest.latitude = 360.0
        cls.PlaceTest.longitude = 180.0
        cls.PlaceTest.amenity_ids = ["4se5dr-6tv39u"]

    def test_subclass_Place(self):
        """Tests if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.PlaceTest.__class__, BaseModel), True)
        self.assertIsInstance(self.PlaceTest, Place)

    def test_attribute_types_Place(self):
        """Tests the attributes of Place"""
        self.assertEqual(type(self.PlaceTest.city_id), str)
        self.assertEqual(type(self.PlaceTest.user_id), str)
        self.assertEqual(type(self.PlaceTest.name), str)
        self.assertEqual(type(self.PlaceTest.description), str)
        self.assertEqual(type(self.PlaceTest.number_rooms), int)
        self.assertEqual(type(self.PlaceTest.number_bathrooms), int)
        self.assertEqual(type(self.PlaceTest.max_guest), int)
        self.assertEqual(type(self.PlaceTest.price_by_night), int)
        self.assertEqual(type(self.PlaceTest.latitude), float)
        self.assertEqual(type(self.PlaceTest.longitude), float)
        self.assertEqual(type(self.PlaceTest.amenity_ids), list)

    def test_save_Place(self):
        """Tests if saving works"""
        self.PlaceTest.save()
        self.assertNotEqual(
            self.PlaceTest.created_at,
            self.PlaceTest.updated_at)

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass
