import sys
import random

from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv)  == 1:
    inp = input("Input: ")

    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print("Output:\n", figlet.renderText(inp))


if len(sys.argv) ==3:

    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

    inp = input("Input: ")

    figlet.setFont(font=sys.argv[2])
    print("Output:\n", figlet.renderText(inp))

else:
    sys.exit("Invalid usage")
