import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

number_lines = 0
try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip().startswith("#"):
                number_lines += 0
            elif line.isspace():
                number_lines += 0
            else:
                number_lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(number_lines)
