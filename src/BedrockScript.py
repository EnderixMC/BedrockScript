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

from argparse import ArgumentParser
from world import World
from lexer import Lexer
from executor import Executor

__version__ = "0.0.1"
credits = f"BedrockScript by v{__version__} EnderixMC (https://github.com/EnderixMC/EwCode)"

parser = ArgumentParser()
parser.add_argument("-v", "--version", action="version", version=f"EwCode {__version__}")
parser.add_argument("--credits", action="version", version=credits, help="show program's credits and exit")
parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode")
parser.add_argument("file", help="the Minecraft region file to execute")
args = parser.parse_args()

try:
    world = World(parser.parse_args().file)
    content = world.load_decoded()

    lexer = Lexer(content)
    lexed = lexer.lex()
    if args.debug:
        print(lexed)
    executor = Executor(lexed)
    executor.execute()
except Exception as e:
    print(f"[{e.__class__.__name__}]: {e}")
    if args.debug:
        raise e