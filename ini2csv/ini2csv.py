from configparser import ConfigParser
import csv
import sys


def ini2csv(args):
    ini_filename = args[0]
    csv_filename = args[1]
    parser = ConfigParser()
    parser.read(ini_filename)
    with open(csv_filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        rows = [
            [section, key, parser[section][key]]
            for section in parser.sections()
            for key in parser[section]
        ]

        csv_writer.writerows(rows)


if __name__ == "__main__":
    ini2csv(sys.argv[1:])
