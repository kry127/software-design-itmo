from src.command import Command


class Echo(Command):
    @staticmethod
    def execute(args):
        """Begin command 'echo' execution."""
        ans = ""
        for arg in args:
            arg = arg.replace("'", "").replace('"', '')
            if ans != "":
                ans = " ".join([ans, arg])
            else:
                ans = "".join([ans, arg])
        return ans
