while True:
    try:
        fraction = input("Fraction: ")
        numerator, denominator = fraction.split("/")

        numerator = int(numerator)
        denominator = int(denominator)

        if numerator > denominator:
            continue
        if denominator == 0:
            continue

        rounded_percentage = round((numerator / denominator) * 100)

        if rounded_percentage <= 1:
            print("E")
        elif rounded_percentage >= 99:
            print("F")
        else:
            print(f"{rounded_percentage}%")

    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
