import random


def main():

    inp_level = get_level()

    score = 0

    numb_math_problems = 0
    for numb_math_problems in range(0, 10):
        a, b = generate_integer(inp_level)
        math_problem = (f"{a} + {b} = ")
        c = a + b

        tries = 0
        while tries < 3:
            users_solution = int(input(math_problem))

            if users_solution == c:
                score = score + 1
                break
            else:
                print("EEE")
                tries = tries + 1

                if tries == 3:
                    print(f"{a} + {b} = {c}")

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                continue

        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
        b = random.randint(0, 9)

    elif level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)

    elif level == 3:
        a = random.randint(100, 999)
        b = random.randint(100, 999)

    return a, b

if __name__ == "__main__":
    main()
