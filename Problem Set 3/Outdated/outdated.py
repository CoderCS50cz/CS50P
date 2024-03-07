months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()

        if date[0].isdigit():
            m, d, y = date.split("/", 2)
            True

        elif date[0].isalpha():
            m_str, d_yr = date.split(" ", 1)
            d, y = d_yr.split(", ", 1)
            True

            if m_str.title() in months:
                m = months.index(m_str) + 1
            else:
                continue
        else:
            continue

        m = int(m)
        d = int(d)
        y = int(y)

        if m < 1 or m > 12:
            continue
        if d < 1 or d > 31:
            continue
        if y < 1 or y > 9999:
            continue

    except ValueError:
        pass

    else:
        break

print(f"{y}-{m:02}-{d:02}")
