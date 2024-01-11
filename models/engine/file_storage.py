#!/usr/bin/python3
"""
a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:
    """
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Defines the class to store and get data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retutns all object"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as f:
            d = {}
            for k, v in FileStorage.__objects.items():
                if isinstance(v, BaseModel):
                    d[k] = v.to_dict()
                else:
                    d[k] = v

            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if not os.path.isfile(FileStorage.__file_path):
                pass
            else:
                with open(FileStorage.__file_path, "r") as f:
                    new_dict = json.load(f)
                    FileStorage.__objects = new_dict
        except Exception as e:
            print(f"An error occurred: {e}")

    def my_classes(self):
        """Returns a dict of valid classes"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        my_classes = {"BaseModel": BaseModel,
                      "User": User,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Place": Place,
                      "Review": Review
                      }
        return my_classes
