#!/usr/bin/python3

import datetime
import json
from os import path
"""
New class FileStorage.
"""


class FileStorage:
    """
    A class that manages the storage of objects in a JSON file..
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add an object to the dictionare __objects.

        Args:
            obj: the object add.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects in JSON file.
        """
        with open(self.__file_path, 'w') as f:
            objetos_serializados = json.dumps(f)
            sel

    def reload(self):
        """
        Deserialize JSON file in  __objects.
        """
        try:

            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                FileStorage.__objects = obj_dict

        except FileNotFoundError:
            pass
