grocery = {}

while True:
    try:
        item = input().lower()

        grocery[item] = grocery.get(item, 0) + 1

    except EOFError:
            print()
            break

    except KeyError:
         pass

for item, count in sorted(grocery.items()):
    print(f"{count} {item.upper()}")
