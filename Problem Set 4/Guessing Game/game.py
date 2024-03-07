import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue

    except ValueError:
        pass
    else:
        break

rand_integ = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue

        if guess < rand_integ:
            print("Too small!")

        elif guess > rand_integ:
            print("Too large!")

        else:
            print("Just right!")
            break

    except ValueError:
        pass
