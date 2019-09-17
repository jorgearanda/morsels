import csv
import sys


def sort_by_column(filename, col):
    with open(filename, 'r') as file:
        reader = csv.reader(file, quotechar="'", delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=False)
        rows = [row for row in reader]

    rows = sorted(rows, key=lambda x: x[int(col)])
    for row in rows:
        print(','.join(row))


if __name__ == "__main__":
    sort_by_column(sys.argv[1], sys.argv[2])
