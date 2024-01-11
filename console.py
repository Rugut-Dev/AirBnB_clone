#!/usr/bin/python3
"""Contaims the entry point of the command interpreter"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
