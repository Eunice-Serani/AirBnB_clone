#!/usr/bin/python3
import json


class FileStorage():
    """ class FileStorage that serializes instances to a json
    file and deserializes JSON file to instances """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary """
        return FileStorage.

    def new(self, obj):
        """ sets in __objects the obj with key obj <class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file(path: __file_path) """
        with open(FileStorage.__file_path, 'w') as file:
            srialzd = {}
            for key, value in self.__objects.items():
                srialzd[key] = value.to_dict()
            json.dump(srialzd, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                json.load(file)
        except Exception:
            pass
