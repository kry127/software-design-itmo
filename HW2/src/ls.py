from src.command import Command
import os


class Ls(Command):
    """This command's purpose is to list files of current working directory (ls)"""
    @staticmethod
    def execute(args=None):
        listfiles = []
        def processListfiles(root, listfiles):
            listfiles = [f for f in listfiles if os.path.exists(os.path.join(root,f))]
            listdir = [f for f in listfiles if os.path.isdir(os.path.join(root,f))]
            listregulars = [f for f in listfiles if os.path.isfile(os.path.join(root,f))]
            return "\n".join(listdir + listregulars)

        if args:
            if (len(args) > 1):
                raise ValueError("bash: cd: too many arguments")
            try:
                return processListfiles(args[0], os.listdir(args[0]))
            except FileNotFoundError:
                raise ValueError(f"bash: cd: file not found {os.path.abspath(args[0])}")
        else:
            try:
                return processListfiles(".", os.listdir("."))
            except FileNotFoundError:
                raise ValueError(f"bash: cd: file not found {os.path.abspath('.')}")