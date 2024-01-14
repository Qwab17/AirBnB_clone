#!/usr/bin/python3
"""
    Module to implement a python command interpreter
    using the cmd module

"""
import cmd
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Simple command interpreter"""
    prompt = "(hbnb) "
    cls_dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
               }

    def precmd(self, line):
        """preprocesses commands"""
        pttn = r'(\w+)\.(\w+)\(\)'
        pttn2 = r'(\w+)\.(\w+)\("([^"]*)"\)'
        pttn3 = r'(\w+)\.(\w+)\("([^"]*)", "([^"]*)", "([^"]*)"\)'
        pttn4 = r'(\w+)\.(\w+)\("([^"]*)", \{([^}]*)\}\)'
        match = re.match(pttn, line)
        match2 = re.match(pttn2, line)
        match3 = re.match(pttn3, line)
        match4 = re.match(pttn4, line)
        if match:
            cls_name, cmnd = match.groups()
            line = f"{cmnd} {cls_name}"
        elif match2:
            cls_name, cmnd, arg = match2.groups()
            line = f"{cmnd} {cls_name} {arg}"
        elif match3:
            cls_name, cmnd, id, attr_n, attr_v = match3.groups()
            line = f"{cmnd} {cls_name} {id} {attr_n} {attr_v}"
        elif match4:
            cls_name, cmnd, id, dct = match4.groups()
            line = f"{cmnd} {cls_name} {id} {dct}"
        return line

    def do_count(self, line):
        """Count counts instances by class name"""
        num = 0
        instances = storage.all()
        for k, v in instances.items():
            lst = k.split('.')
            if lst[0] == line:
                num += 1
        print(num)

    def do_quit(self, line):
        """Quit command to exit program"""
        return True

    def do_EOF(self, line):
        """Handle EOF character - ctrl+D to quit"""
        print()
        return True

    def help_help(self):
        """Prints help command description"""
        print("Provides command description")

    def emptyline(self):
        """Prints nothing to the console"""
        pass

    def do_create(self, line):
        """create command to create new instance"""
        if not line:
            print("** class name missing **")
            return
        elif line not in HBNBCommand.cls_dct:
            print("** class doesn't exist **")
            return
        else:
            instance = HBNBCommand.cls_dct[line]()
            print(instance.id)
            instance.save()

    def do_show(self, line):
        """Prints string representation of an instance"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.cls_dct:
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
        """Deletes an instance base on class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.cls_dct:
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
                storage.save
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of instances
        based or not on the classname"""
        instances = storage.all()
        args = line.split()
        if args[0] in HBNBCommand.cls_dct:
            for instance in instances.values():
                print(str(instance))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates instances based on class name and id"""
        args = shlex.split(line)
        if not line:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.cls_dct:
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
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
