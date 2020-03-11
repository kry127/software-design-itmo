from src.command import Command
import sys


class Exit(Command):
    """Exit CLI emulator"""
    @staticmethod
    def execute():
        sys.exit()
