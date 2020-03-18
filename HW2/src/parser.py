from src.cat import Cat
from src.echo import Echo
from src.exit import Exit
from src.pwd import Pwd
from src.wc import Wc
from src.cd import Cd
from src.ls import Ls
from collections import defaultdict
import re

EQ = '='
PIPE = '|'
DOL = '$'


class Parser:
    """
    Command and arguments parser,
    called in main.py to process all user inputs and print the outputs.
    """
    def __init__(self):
        self.globals = defaultdict()
        self.command = defaultdict()
        self.command["cat"] = Cat.execute
        self.command["echo"] = Echo.execute
        self.command["exit"] = Exit.execute
        self.command["pwd"] = Pwd.execute
        self.command["wc"] = Wc.execute
        self.command["cd"] = Cd.execute
        self.command["ls"] = Ls.execute

    def parse(self, line):
        """
        Parse user input into command and arguments,
        call command with arguments and print an output.
        """
        # TODO: dollar $ substitution
        line = line.strip('\n')
        line = re.sub(r"^\s+|\s+$", "", line)
        line = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''', line)
        if len(line) == 1:
            # it's either single function of function, awaiting arguments
            line = line[0].split(EQ)
            if len(line) == 1:
                line = line[0]
                command = self.parse_command(line)
                if command:
                    print(command(), end='\n')
                elif len(line) > 1 and line[0] == DOL and line[1:] in self.globals.keys():
                    key = line[1:]
                    val = self.globals[key]
                    command = self.parse_command(val)
                    if command:
                        print(command(), end='\n')
                    else:
                        print(val, end='\n')
                else:
                    print("Command {} is not found\n".format(line))

            else:
                var, arg = line[0], line[1]
                self.globals[var] = arg
        else:
            for i in range(len(line)):
                for key, val in self.globals.items():
                    line[i] = line[i].replace("${}".format(key), val)

            c, args = line[0], line[1:]
            command = self.parse_command(c)
            if command:
                if PIPE in args:
                    # if pipe was in arguments and was valid, it was split
                    piped_args = []
                    new_args = []
                    for arg in args:
                        if arg != PIPE:
                            piped_args.append(arg)
                        else:
                            piped_args.append(new_args)
                            new_args = []
                    c_args, other_args = piped_args[0], piped_args[1:]
                    # notice that we only have commands to be piped, or the arguments are incorrect
                    try:
                        result = command(c_args)
                    except ValueError or TypeError:
                        print("Incorrect arguments\n: {}".format(c_args))
                        return

                    for arg in other_args:
                        try:
                            command = self.parse_command(arg)
                            result = command(result)
                        except ValueError or TypeError:
                            print("Incorrect arguments: {}\n".format(result))
                            return

                    print(result, end='\n')
                else:
                    try:
                        result = command(args)
                        print(result, end='\n')
                    except ValueError:
                        print("Incorrect arguments: {}\n".format(args))
            else:
                print("Command {} is not found\n".format(line))

    def parse_command(self, command):
        """
        Parse command (if correct) or return None otherwise.
        """
        if command in self.command.keys():
            return self.command[command]
        return None
