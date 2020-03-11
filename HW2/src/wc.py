from src.command import Command
import os.path


class Wc(Command):
    @staticmethod
    def execute(args):
        """Begin command 'wc' execution."""

        if len(args) == 1:
            path = args[0]
            path = path.replace("'", "").replace('"', '')
            if os.path.exists(path):
                chars = 0
                words = 0
                lines = 0

                with open(path, 'r') as file:
                    for line in file:
                        lines += 1
                        words += len(line.split())
                        chars += len(line)

                return "{} {} {}".format(lines, words, chars)
        raise ValueError
