#!/usr/bin/python3
"""
    Module that implements a basic command interpreter
    entry point

"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


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

    def do_create(self, line):
        """Creates a new instance of BaseModel."""
        if not line:
            print("** class name missing **")
            return
        elif line not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints string representation of an instance
        by class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            instances = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class namd and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            instances = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on class name"""
        args = line.split()
        instances = storage.all()
        if not line or args[0] in ["BaseModel", "User"]:
            for instance in instances.values():
                print(str(instance))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on class name and id"""
        args = shlex.split()
        if not line:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        else:
            instances = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in instances:
                instance = instances[key]
                if args[2] not in ['id', 'created_at', 'updated_at']:
                    try:
                        value = eval(args[3])
                        if isinstance(value, (int, float, str)):
                            setattr(instance, args[2], value)
                            instance.save()
                        else:
                            print("** invalid value type **")
                    except (SyntaxError, NameError):
                        setattr(instance, args[2], args[3])
                        instance.save()
                    else:
                        print("** attribute can't be updated **")
                else:
                    print("** no instance fount **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
