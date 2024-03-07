def main():
    inp_fraction = input("Fraction: ")

    pr = convert(inp_fraction)
    volume = gauge(pr)

    print(volume)


def convert(fraction):
    fraction = fraction.split("/")
    x, y = fraction

    if not x.isdigit() or not y.isdigit():
        raise ValueError

    x = int(x)
    y = int(y)
    percentage = round((x / y) * 100)

    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        percentage = f"{percentage}%"
        return percentage


if __name__ == "__main__":
    main()
