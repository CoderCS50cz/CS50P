from datetime import date
import sys
import re
import inflect


def main():
    print(convert(input("Date of Birth: ").strip()))


def convert(dob):
    try:
        if not re.search(r"^[\d]{4}-[\d]{2}-[\d]{2}$", dob):
            sys.exit("Invalid date")

        y, m, d = dob.split("-")
        day_of_b  = date(int(y), int(m), int(d))

        age = minutes_format(day_of_b)

    except ValueError:
        sys.exit("Invalid date")
    else:
        return age


def minutes_format(day_of_b):
    today = date.today()
    difference = today - day_of_b
    leap_diff = difference.days * 24 * 60

    p = inflect.engine()
    age_in_min = p.number_to_words(leap_diff, andword="")
    minutes = p.plural("minute")

    return age_in_min.capitalize() + " " + minutes


if __name__ == "__main__":
    main()
