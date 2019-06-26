def parse_fixed_width_file(input, ranges):
    result = []
    for line in input:
        res_line = []
        for r in ranges:
            res_line.append(line[r[0]:r[1]].strip())
        result.append(res_line)
    
    return result


def parse_columns(input):
    ranges = []
    for r in input.split(','):
        start, end = r.split(':')
        ranges.append((int(start), int(end)))
    
    return ranges


def main(args):
    ranges = parse_columns(args[2][7:])
    with open(args[0]) as text_file:
        output = parse_fixed_width_file(text_file, ranges)

    with open(args[1], 'w') as csv_file:
        for line in output:
            csv_file.write(','.join(line) + '\n')
