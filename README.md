# BedrockScript
## Description
An esoteric programming language written in Python that makes you write code in Minecraft[^1][^2]. Get ready for pain
## Usage
1. Write some code
2. Convert the code to binary
2. In Minecraft, create a new world
3. Write the binary in the world by breaking bedrock at Y 0 from X 0 onwards (Air blocks equal 0 and bedrock blocks equal 1)
4. Signal the end of your code by placing a barrier after the last bedrock/air block (Still at Y 0)
5. Save and exit the world
6. Run `python BedrockScript.py "{FILE}"` (Replace {FILE} with the full path of your world's region file - e.g. %APPDATA%\.minecraft\saves\New World\region\r.0.0.mca)

[^1]: BedrockScript only works for Minecraft Java Edition, NOT Minecraft Bedrock Edition, even though it has "Bedrock" in it's name
[^2]: BedrockScript has only been tested on Minecraft Java Edition 1.14.4 - Other versions of Minecraft Java Edition might not work
