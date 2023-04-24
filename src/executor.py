"""
BedrockScript - executor.py

@author: EnderixMC
"""

from lib import commands, variables

class Executor:
    def __init__(self, lexed):
        self.lexed = lexed
    def execute(self):
        lexed = self.lexed
        for line in lexed:
            command = line[0][1]
            args = line[1:]
            for i in commands:
                if i.name == command:
                    for i2 in range(len(args)):
                        arg = args[i2]
                        if arg[0] == "VAR":
                            args[i2] = ("STRING",variables.get(arg[1]))
                    i(args).execute()
                    break