#!/usr/bin/python3
""" FileStoage unit tests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage """

    def test_all_FileStorage(self):
        """Tests if all is functional in File Storage"""
        store = FileStorage()
        dict_instances = store.all()
        self.assertIsNotNone(dict_instances)
        self.assertEqual(type(dict_instances), dict)
        self.assertIs(dict_instances, store._FileStorage__objects)

    def test_new_FileStorage(self):
        """Tests when new is created in File Storage"""
        store = FileStorage()
        item = store.all()
        user = User()
        user.id = 22475
        user.name = "Betty"
        store.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(item[key])

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
