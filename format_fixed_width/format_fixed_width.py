def format_fixed_width(rows, padding=2, widths=None, alignments=None):
    if widths is None:
        widths = find_widths(rows, padding)
    result = ""
    for row in rows:
        for idx, item in enumerate(row):
            if alignments is None or alignments[idx] != "R":
                result += item.ljust(widths[idx])
            else:
                result += item.rjust(widths[idx])
            if idx < len(row):
                result += " " * padding
        result = result.strip() + "\n"

    return result.strip()


def find_widths(rows, padding=2):
    widths = []
    for row in rows:
        for idx, item in enumerate(row):
            if len(widths) < idx + 1:
                widths.append(len(item))
            widths[idx] = max(widths[idx], len(item))

    return widths
