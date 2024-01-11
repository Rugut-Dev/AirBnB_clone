#!/usr/bin/python3
"""Contaims the entry point of the command interpreter"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        return cmd.Cmd.emptyline(self)

    def help_quit(self):
        print("Quit command to exit the program \n\n")

    def help_EOF(self):
        print("Quit!!!")

    def do_create(self, line):
        """Create a new instance of BaseModel, save it and print id"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.my_classes():
            print("** class doesn't exist **")
        else:
            new_instance = storage.my_classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string rep of an inst based on the class name & id"""
        args = line.split(' ')
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.my_classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(' ')
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.my_classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg != "":
            args = arg.split(' ')
        class_name = args[0]
        if class_name not in storage.my_classes():
            print("** class doesn't exist **")
            return
        else:
            lst = [str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == args[0]]
            print(lst)
    else:
        lst = [str(obj) for key, obj in storage.all().items()]
        print(lst)


    def do_all(self, arg):
        """Prints all string representations of all instances"""
    if arg != "":
        args = arg.split(' ')
        class_name = args[0]
        if class_name not in storage.my_classes():
            print("** class doesn't exist **")
            return
        else:
            lst = [str(obj) for key, obj in storage.all().items() 
                    if type(obj).__name__ == args[0]]
            print(lst)
    else:
        lst = [str(obj) for key, obj in storage.all().items()]
        print(lst)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
