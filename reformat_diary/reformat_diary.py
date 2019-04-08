import re
import sys

date_regex = r'\d{4}\-\d{2}\-\d{2}\n'

def entries_by_date(file):
    raw_contents = file.read()
    contents = _handle_html(raw_contents)
    dates = [date.strip() for date in re.findall(date_regex, contents)]
    texts = [text.strip() for text in re.split(date_regex, contents)[1:]]
    return zip(dates, texts)


def _handle_html(input):
    mappings = [('&quot;', '"'), ('&nbsp;', ' '), ('&amp;', '&')]
    for mapping in mappings:
        input = input.replace(mapping[0], mapping[1])
    return input


def main(input):
    with open(input, 'r') as file:
        entries = entries_by_date(file)

    for entry in entries:
        date, text = entry
        filename = date + '.txt'
        with open(filename, 'w') as entry_file:
            entry_file.write(text)
            print(date + '.txt written')


if __name__ == '__main__':
    main(sys.argv[1:])
