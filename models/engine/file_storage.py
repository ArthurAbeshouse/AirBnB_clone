#!/usr/bin/python3
""" File Storage """
from models.base_model import BaseModel
import json
import models
import copy


class FileStorage():
    """ File Storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ All """
        return self.__objects

    def new(self, obj):
        """ New """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ Save """
        newDict = {}
        for x, y in copy.deepcopy(self.__objects).items():
            newDict[x] = y.to_dict()
        data = json.dumps(newDict)
        with open(self.__file_path, 'w') as f:
            f.write(data)

    def reload(self):
        """ Reload """
        newDict2 = {}
        try:
            with open(self.__file_path) as f:
                loadedString = f.read()
                newDict2 = json.loads(loadedString)
                for x, y in newDict2.items():
                    newDict2[x] = BaseModel(y)
                self.__objects = newDict2
        except FileNotFoundError:
            pass
