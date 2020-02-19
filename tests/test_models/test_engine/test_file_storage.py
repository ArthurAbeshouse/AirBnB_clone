#!/usr/bin/python3
""" FileStoage unit tests """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ Tests FileStorage """

    def test_FileStorage(self):
        """pass"""
        pass

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
