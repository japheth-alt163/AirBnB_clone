#!/usr/bin/python3
"""
Module for FileStorage class.
"""

import json

class FileStorage:
    """
    FileStorage class for serializing instances to a JSON file and deserializing JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects (only if the JSON file (__file_path) exists).
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**obj)
        except FileNotFoundError:
            pass
