#!/usr/bin/python3

from os import path
import json
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
        return self.__objects

    def new(self, obj):
        """
        Add an object to the dictionare __objects.

        Args:
            obj: the object add.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects dictionary to a JSON file.
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(new_dict))

    def reload(self):
        """
        Deserialize JSON file to  __objects dictionary.
        """

        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.state import State

        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                for value in json.loads(file.read()).values():
                    eval(value["__class__"])(**value)
