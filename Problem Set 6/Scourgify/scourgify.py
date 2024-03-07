import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    csv_file_before = sys.argv[1]
    csv_file_after = sys.argv[2]


students = []

try:
    with open(csv_file_before) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            house = row["house"]
            students.append({"first": first, "last": last, "house": house})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


with open(csv_file_after, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)
