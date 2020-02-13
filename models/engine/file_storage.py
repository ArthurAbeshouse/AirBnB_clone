#!/usr/bin/python3
""" File Storage """
import models.base_model as bm
import json


class FileStorage():
    """ File Storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ All """
        return self.__objects

    def new(self, obj):
        """ New """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]

    def save(self):
        """ Save """
        data = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as f:
            f.write(data)

    def reload(self):
        """ Reload """
        try:
            with open(self.__file_path) as f:
                loadedString = f.read()
                self.__objects = json.loads(loadedString)
        except FileNotFoundError:
            pass
