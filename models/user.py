#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """ User class """

    def __init__(self, *args, **kwargs):
        """ Initializes User instance """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        """ Returns the string representation of User """
        return "[{}] ({}) {} {}".format(self.__class__.__name__, self.id, self.first_name, self.last_name)
