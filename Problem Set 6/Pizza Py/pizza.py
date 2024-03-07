import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    csv_file = sys.argv[1]

table = []

try:
    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(table, headers="firstrow", tablefmt="grid"))
