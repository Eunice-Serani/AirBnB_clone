#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """ class BaseModel that defines all common
    attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """entry point"""
        if kwargs is not None and kwargs.get('id') is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        self.__setattr__(key, datetime.fromisoformat(value))
                    else:
                        self.__setattr__(key, value)

        else:
            self.id = str(uuid4())
            # current datetime when an instance is created
            self.created_at = datetime.now()
            # when instance is created and updated every time object is changed
            self.updated_at = self.created_at

    def save(self):
        """updates the public instance attribute update_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        ky = {key: value for key, value in self.__dict__.items()}
        ky['__class__'] = self.__class__.__name__
        ky['created_at'] = self.created_at.isoformat()
        ky['updated_at'] = self.updated_at.isoformat()
        return ky

    def __str__(self):
        """string representation"""
        cl_name = self.__class__.__name__
        ky = {key: value for key, value in self.__dict__.items()}
        return("[{}] ({}) {}".format(cl_name, self.id, ky))
