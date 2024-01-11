#!/usr/bin/python3
"""
a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:
    """
import json
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
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
                FileStorage.__objects = new_dict
        except FileNotFoundError:
            return
