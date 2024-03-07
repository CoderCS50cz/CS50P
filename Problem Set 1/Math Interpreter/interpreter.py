inter = input("Expression: ")

x, y, z = inter.split(" ")

if y == "+":
    print(float(x) + float(z))
if y == "-":
    print(float(x) - float(z))
if y == "*":
    print(float(x) * float(z))
if y == "/" and z != 0:
    print(float(x) / float(z))
