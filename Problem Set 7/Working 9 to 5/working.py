import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r"^([0-9]{1,2}):?([0-9]{1,2})?\s+(AM|PM)\s+to\s+([0-9]{1,2}):?([0-9]{1,2})?\s+(AM|PM)$", s):
        hours_am = int(matches.group(1))
        min_am = matches.group(2)
        am_pm = matches.group(3)
        hours_pm = int(matches.group(4))
        min_pm = matches.group(5)
        pm_am = matches.group(6)

        if hours_am > 12 or hours_pm > 12:
            raise ValueError
        if (min_am or min_pm) != None and (int(min_am) or int(min_pm)) > 59:
             raise ValueError

        shift_start = tw_four_format(hours_am, min_am, am_pm)
        shift_finish = tw_four_format(hours_pm, min_pm, pm_am)
        convert_format = shift_start + " to " + shift_finish
        return convert_format

    else:
         raise ValueError


def tw_four_format(hours, minutes, meridiem):

        if meridiem == "PM" and hours != 12:
             hours = hours + 12
        if meridiem == "AM" and hours == 12:
             hours = 0
        if minutes == None:
             minutes = 0
        return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
