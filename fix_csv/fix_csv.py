import csv
from docopt import docopt


usage = """
Fix the formatting of a CSV file

Usage:
    fix_csv.py INPUT OUTPUT [--in-delimiter=<delimiter>] [--in-quote=<quote>]

Options:
    --in-delimiter=<delimiter>  Input delimiter
    --in-quote=<quote>          Input quote symbol
"""


def fix_csv(args):
    delimiter = args['--in-delimiter']
    quotechar = args['--in-quote']
    with open(args['INPUT']) as in_file, open(args['OUTPUT'], 'w') as out_file:
        if delimiter is None and quotechar is None:
            dialect = csv.Sniffer().sniff(
                in_file.read(300), delimiters='| \t,')
            in_file.seek(0)
            delimiter = dialect.delimiter if delimiter is None else delimiter
            quotechar = dialect.quotechar if quotechar is None else quotechar

        reader = csv.reader(in_file, delimiter=delimiter, quotechar=quotechar)
        writer = csv.writer(out_file)
        for row in reader:
            writer.writerow(row)


if __name__ == '__main__':
    args = docopt(usage, argv=None)
    fix_csv(args)
