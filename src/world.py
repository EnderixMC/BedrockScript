"""
BedrockScript - world.py

@author: EnderixMC
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