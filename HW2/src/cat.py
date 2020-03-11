from src.command import Command
import os.path


class Cat(Command):
    @staticmethod
    def execute(args):
        """Begin command 'cat' execution."""
        print(args)
        if len(args) == 1:
            path = args[0]
            path = path.replace("'", "").replace('"', '')
            if os.path.exists(path):
                with open(path, 'r') as file:
                    data = file.read()
                    return data
        raise ValueError
