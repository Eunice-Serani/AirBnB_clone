#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """ FileStorage class """

    __file_path = "file.json"
    __objects = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            if key != "BaseModel":
                serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the file exists) """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_class = FileStorage.__objects[class_name]
                    obj_instance = obj_class(**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
