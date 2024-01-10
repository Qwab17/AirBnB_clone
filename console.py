#!/usr/bin/python3
"""
    Module that implements a basic command interpreter
    entry point

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class the implements a python command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """Ctrl + D to exit program"""
        print()
        return True

    def emptyline(self):
        """Prints an empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
