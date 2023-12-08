#!/usr/bin/python3
"""
Console module
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """
    Console class
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User}

    def emptyline(self):
        """
        Empty line method
        """
        pass

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """
        print()
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.classes[args]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(arg_list[0], arg_list[1])
        objects = FileStorage().all()
        if obj_key not in objects:
            print("** no instance found **")
            return
        print(objects[obj_key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(arg_list[0], arg_list[1])
        objects = FileStorage().all()
        if obj_key not in objects:
            print("** no instance found **")
            return
        del objects[obj_key]
        FileStorage().save()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        """
        objects = FileStorage().all()
        if not args:
            print([str(objects[obj]) for obj in objects])
            return
        arg_list = args.split()
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        print([str(objects[obj]) for obj in objects if arg_list[0] in obj])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        obj_key = "{}.{}".format(arg_list[0], arg_list[1])
        objects = FileStorage().all()
        if obj_key not in objects:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return

        setattr(objects[obj_key], arg_list[2], arg_list[3])
        objects[obj_key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
