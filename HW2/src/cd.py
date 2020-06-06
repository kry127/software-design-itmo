from src.command import Command
import os


class Cd(Command):
    """This command's purpose is for changing current working directory (wd)"""
    @staticmethod
    def execute(args=None):
        if not args:
            return ""
        if len(args) > 1:
            raise ValueError("bash: cd: too many arguments")

        try:
            os.chdir(args[0])
        except FileNotFoundError:
            raise ValueError("bash: cd: file not found error")
