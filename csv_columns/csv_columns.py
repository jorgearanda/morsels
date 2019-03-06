from collections import defaultdict
import csv

def csv_columns(input, headers=None, missing=None):
    """Return a dictionary with a column per csv field in the input."""
    def get_headers():
        if headers is None:
            return next(reader)
        else:
            return headers

    def column_for(index):
        return columns[headers[index]]

    def fill_blanks_in(line):
        if len(line) < len(headers):
            line.extend([missing] * (len(headers) - len(line)))
        return line

    reader = csv.reader(input)
    headers = get_headers()
    columns = defaultdict(list)
    for line in reader:
        line = fill_blanks_in(line)
        for index, value in enumerate(line):
            column_for(index).append(value)

    return columns
