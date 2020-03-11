class Command:
    """The Command interface"""

    @staticmethod
    def execute(*args):
        """Begin command execution"""
        raise NotImplementedError()
