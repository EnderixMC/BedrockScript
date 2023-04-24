"""
    BedrockScript - An esoteric programming language written in Python that makes you write code in Minecraft
    Copyright (C) 2023  EnderixMC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

class Variables:
    def __init__(self):
        self.variables = {}
    def set(self, name, value):
        self.variables[name] = value
    def set_multi(self, values):
        for i in values:
            self.variables[str(i)] = str(values[i])
    def remove(self, name):
        del self.variables[name]
    def get(self, name):
        return self.variables[name]

class Command:
    name = ""
    def __init__(self, args):
        self.args = args
        if not self.check_args():
            raise SyntaxError(f"Invalid arguments for command {self.name}: {args}")
    def __str__(self): # For debugging
        return f"Command({self.name}, {self.args})"
    def __repr__(self): # For debuggings
        return f"Command({self.name}, {self.args})"
    def execute(self):
        pass
    def check_args(self):
        pass

class PrintCommand(Command):
    name = "print"
    def execute(self):
        for i in self.args:
            print(i[1], end="")
        print()
    def check_args(self):
        return len(self.args) > 0 and all(i[0] == "STRING" for i in self.args)

class Set(Command):
    name = "set"
    def execute(self):
        variables.set_multi(self.args[0][1])
    def check_args(self):
        return len(self.args) == 1 and self.args[0][0] == "NBT"

commands = [PrintCommand,Set]
variables = Variables()