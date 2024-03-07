import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if matches:
        if int(matches.group(1)) in range(0, 256) and int(matches.group(2)) in range(0, 256) and int(matches.group(3)) in range(0, 256) and int(matches.group(4)) in range(0, 256):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
