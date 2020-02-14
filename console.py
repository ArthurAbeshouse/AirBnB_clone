#!/usr/bin/python3
"""Console for AirBnB project"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quits the program"""
        return True

    def emptyline(self):
        """Does nothing if the user presses ENTER"""
        pass

    def do_EOF(self, line):
        """Quits the program at end of the file"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
