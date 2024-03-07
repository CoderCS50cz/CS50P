def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
       return False

    numbers_started = False
    for i in range(2, len(s)):
        if not s[i].isalnum():
            return False
        if s[i].isdigit():
            if not numbers_started and s[i] == '0':
                return False
            numbers_started = True
        elif s[i].isalpha() and numbers_started:
            return False

    if not s.isalnum():
        return False

    return True

main()
