#!/usr/bin/python3
""" console module """

import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class """
    prompt = '(hbnb) '

    def do_create(self, arg):
        """ Creates a new instance of BaseModel and saves it to the JSON file """
        if not arg:
            print("** class name missing **")
            return
        classes = ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]
        if arg not in classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class name and id """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id (save the change into the JSON file) """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        if key in objects:
            del objects[key]
            FileStorage().save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = FileStorage().all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj_instance = objects[key]
        setattr(obj_instance, args[2], eval(args[3]))
        obj_instance.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name """
        objects = FileStorage().all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review", "User"]:
                print("** class doesn't exist **")
                return
            filtered_objects = {k: v for k, v in objects.items() if args[0] in k}
            print([str(obj) for obj in filtered_objects.values()])

    def do_quit(self, arg):
        """ Exits the program """
        return True

    def do_EOF(self, arg):
        """ Exits the program when End-Of-File is reached """
        print("")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
