def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False

    if len(s) > 6 or len(s) < 2:
        return False

    numb_start = False
    for i in range(2, len(s)):
        if not s[i].isalnum():
            return False
        if s[i].isdigit():
            if not numb_start and s[i] == "0":
                return False
            numb_start = True
        elif s[i].isalpha() and numb_start:
            return False

    if not s.isalnum():
        return False

    return True



if __name__ == "__main__":
    main()
