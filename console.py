#!/usr/bin/python3
""" console module """

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ subclass of Cmd class """
    valid_classes = ["BaseModel"]
    prompt = '(hbnb) '
    # def _init_(self):
    #     """ HBNB constructor """
    #     super()._init_()
    #     self.prompt = '(hbnb) '

    def do_EOF(self, line):
        """ EOF function """
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """
        Overload emptyline of superclass
        to make it not print the previous command
        if line is empty
        """
        pass

    def do_create(self, obj_name):
        """Creates a new instance of BaseModel"""
        if not obj_name:
            print("** class name missing **")
        elif obj_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            # instance = globals()[obj_name]()
            instance = eval(obj_name)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split(' ')
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in HBNBCommand.valid_classes:
            key = ".".join([args[0], args[1]])
            dc = storage.all()
            if key in dc:
                print(dc[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in HBNBCommand.valid_classes:
            key = ".".join(args)
            dc = storage.all()
            if key in dc:
                del dc[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        if not line:
            dc = storage.all()
            li = [value._str_() for value in dc.values()]
            print(li)
        else:
            if line in HBNBCommand.valid_classes:
                dc = storage.all()
                li = []
                for value in dc.values():
                    if value._class.__name_ == line:
                        li.append(value._str_())
                print(li)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        length = len(args)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif length >= 2:
            key = ".".join(args[:2])
            dc = storage.all()
            if key in dc:
                try:
                    if args[2]:
                        try:
                            if args[3]:
                                if type(eval(args[3])) in [str, int, float]:
                                    dc[key]._setattr_(args[2], eval(args[3]))
                                    dc[key].save()
                        except IndexError:
                            print("** value missing **")
                except IndexError:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")

    def default(self, line):
        """ default action if command not valie """
        try:
            eval(line)
        except Exception as e:
            print(f"Error: {e}")


if _name_ == '_main_':
    HBNBCommand().cmdloop()
