import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    word = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(word)


if __name__ == "__main__":
    main()
