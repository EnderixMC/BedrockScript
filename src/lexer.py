"""
BedrockScript - lexer.py

@author: EnderixMC
"""

import json
import re

class Lexer:
    DIGITS = "0123456789"
    def __init__(self, raw):
        self.raw = raw
    def lex(self):
        raw = self.raw
        raw = raw.split("\n")
        final = []
        skips = 0
        for i in range(len(raw)):
            #Check if a skip is needed
            if skips > 0:
                skips -= 1
                continue
            #Initialize variables
            line = raw[i]
            line_lex = []
            lexeme_count = 0
            #Check if line is a valid command
            search1 = re.search("^/[a-z]+$", line, re.IGNORECASE)
            search2 = re.search("^/[a-z]+[ .+$]+", line, re.IGNORECASE)
            if not search1 and not search2:
                raise Exception(f"Invalid syntax (Line {i}): {line}")
            #Get command name
            command = line.split(" ")[0][1:]
            line_lex.append(("COMMAND",command))
            #Check if command has no arguments
            if search1 and not search2:
                final.append(line_lex)
                continue
            lexeme_count += len(command)+2
            #Get arguments
            while lexeme_count < len(line):
                lexeme = line[lexeme_count]
                if lexeme == "'" or lexeme == '"': # Lex string
                    typ, tok, consumed = self.lex_string(line[lexeme_count:])
                    line_lex.append((typ, tok))
                    lexeme_count += consumed
                elif lexeme in self.DIGITS: # Lex number
                    typ, tok, consumed = self.lex_number(line[lexeme_count:])
                    line_lex.append((typ, tok))
                    lexeme_count += consumed
                elif lexeme == "[":
                    typ, tok, consumed = self.lex_var(line[lexeme_count:])
                    line_lex.append((typ, tok))
                    lexeme_count += consumed
                elif lexeme == "{": # Lex NBT (JSON)
                    typ, tok, consumed = self.lex_nbt(line[lexeme_count:])
                    line_lex.append((typ, tok))
                    lexeme_count += consumed
                elif lexeme == " ":
                    lexeme_count += 1
                    continue
                else:
                    raise Exception(f"Invalid syntax (Line {i}, Pos {lexeme_count}): {lexeme}")
            #Append line_lex to final
            final.append(line_lex)
        return final
    def lex_string(self, line):
        delim = line[0]
        copy = line
        line = line[1:]
        while True:
            if line[0] == "\\":
                line = line[2:]
            elif line[0] == delim:
                break
            else:
                line = line[1:]
        return ("STRING", copy[1:len(copy)-len(line)], len(copy)-len(line)+1)
    def lex_number(self, line):
        consumed = 0
        dots = 0
        for c in line:
            if c in self.DIGITS+".":
                if c == ".":
                    dots += 1
                    if dots > 1:
                        break
                consumed += 1
            else:
                break
        if dots == 0:
            return ("INT", int(line[:consumed]), consumed)
        return ("FLOAT", float(line[:consumed]), consumed)
    def lex_var(self, line):
        line = line[1:]
        string = ""
        for c in line:
            if c == "]":
                break
            else:
                string += c
        return ("VAR", string, len(string)+2)
    def lex_nbt(self, line):
        extras = 0
        consumed = 0
        for c in line:
            consumed += 1
            if c == "{":
                extras += 1
            elif c == "}":
                if extras > 0:
                    extras -= 1
                else:
                    break
        string = line[:consumed]
        final = json.loads(string)
        return ("NBT", final, consumed)