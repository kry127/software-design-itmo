from src.command import Command
import os


class Ls(Command):

    """Augmentation function for traversing files in `root` folder.
    It reads the `list_files` and returns string with directories and then regular files
    separated by '\n' character"""
    @staticmethod
    def _process_list_files(root, list_files):
        list_files = [f for f in list_files if os.path.exists(os.path.join(root, f))]
        listdir = [f for f in list_files if os.path.isdir(os.path.join(root, f))]
        list_regulars = [f for f in list_files if os.path.isfile(os.path.join(root, f))]
        return "\n".join(listdir + list_regulars)

    """This command's purpose is to list files of current working directory (ls)"""
    @staticmethod
    def execute(args=None):

        if args and len(args) > 1:
            raise ValueError("bash: cd: too many arguments")

        search_path = args[0] if args else "."
        try:
            return Ls._process_list_files(search_path, os.listdir(search_path))
        except FileNotFoundError:
            raise ValueError(f"bash: cd: file not found {os.path.abspath(search_path)}")
