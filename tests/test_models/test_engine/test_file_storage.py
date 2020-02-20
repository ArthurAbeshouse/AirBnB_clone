#!/usr/bin/python3
""" FileStoage unit tests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import pep8


class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage """

    @classmethod
    def setUp(cls):
        """Sets up testing methods"""
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.user.email = "BettyHolberton@holbertonschool.com"
        cls.storage = FileStorage()
        cls.path = "file.json"

    @classmethod
    def teardown(cls):
        """Tears down the test"""
        del cls.user
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Removes json file"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_FileStorage(self):
        """Tests docstrings"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        
    def test_save_FileStorage(self):
        """Tests if saving works"""
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_all_FileStorage(self):
        """Tests if all is functional in File Storage"""
        storage = FileStorage()
        dict_instances = storage.all()
        self.assertIsNotNone(dict_instances)
        self.assertEqual(type(dict_instances), dict)
        self.assertIs(dict_instances, storage._FileStorage__objects)

    def test_new_FileStorage(self):
        """Tests when new is created in File Storage"""
        storage = FileStorage()
        item = storage.all()
        user = User()
        user.id = 22475
        user.name = "Betty"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(item[key])

    def test_reload_FileStorage(self):
        """Tests reload in File Storage"""
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except BaseException:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines_2 = f.readlines()
        self.assertEqual(lines, lines_2)
        try:
            os.remove(path)
        except BaseException:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
