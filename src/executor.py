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