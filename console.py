#!/usr/bin/python3
""" Program Console contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):

    """ prompt message """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """ command to exit the console """
        return True

    def emptyline(self):
        """ print emptyline """
        pass

    def do_quit(self, line):
        """ command to exit the console """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
