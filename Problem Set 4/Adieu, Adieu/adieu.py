import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        break

print(f"\nAdieu, adieu, to {p.join(names)}")
