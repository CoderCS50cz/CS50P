import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(r"^.+https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+).+", s, re.IGNORECASE):
       return "https://youtu.be/" + matches.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
