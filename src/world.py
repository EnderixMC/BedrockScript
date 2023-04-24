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

import binascii
import anvil
import os.path

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

class InvalidWorldFileError(Exception):
    pass

class World:
    def __init__(self, file):
        self.file = os.path.abspath(file)
        try:
            self.region = anvil.Region.from_file(self.file)
        except FileNotFoundError:
            raise InvalidWorldFileError("The file specified does not exist:", self.file)
    def load(self):
        final = ""
        chunk = 0
        running = True
        while running:
            try:
                self.chunk = anvil.Chunk.from_region(self.region, chunk, 0)
            except IndexError:
                raise InvalidWorldFileError("The file specified is not a valid world file:", self.file)
            for i in range(16):
                block = self.chunk.get_block(i, 0, 0)
                if block.id == "barrier":
                    running = False
                    break
                if block.id == "air":
                    final += "0"
                elif block.id == "bedrock":
                    final += "1"
                else:
                    raise Exception("Unknown block: " + block.id)
            chunk += 1
        return final
    def load_decoded(self):
        return decode_binary_string(self.load())