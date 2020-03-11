from src.command import Command
import re
import glob


class Grep(Command):
    @staticmethod
    def execute(args):
        """Begin command 'grep' execution."""
        pattern, files = args
        for arg in args:
            for file in glob.iglob(arg):
                for line in open(file, 'r'):
                    if re.search(pattern, line):
                        print(line, end='')
