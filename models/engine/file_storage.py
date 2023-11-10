#!/usr/bin/python3
"""defines the FileStorage class
"""

import json


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
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj


    def save(self):
        """
        Serialize __objects dictionary to a JSON file.
        """
        data = {}
        for k, obj in FileStorage.__objects.items():
            data[k] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """
        Deserialize JSON file to  __objects dictionary.
        """

        try:
            with open(FileStorage.__file_path, "r") as json_file:
                objeto_rec = json.load(json_file)
                for k, v in objeto_rec.items():
                    from models.base_model import BaseModel
                    FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            return

    def attributes(self):
        """
        return a dict of attributes for diferent class
        """

        attributes = {
                "BaseModel":{
                    "id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime
                    },
                "User": {
                    "email": str,
                    "pasword": str,
                    "first_name": str,
                    "last_name": str
                    },
        }
        return attributes
