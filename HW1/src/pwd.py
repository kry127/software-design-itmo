from src.command import Command
import os


class Pwd(Command):
    """Begin command 'pwd' execution."""
    @staticmethod
    def execute():
        return os.getcwd()
