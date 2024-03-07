camel = input("camelCase: ")

snake_case = ""

print("snake_case:", snake_case, end="")

for c in camel:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c.lower(), end="")
print()
