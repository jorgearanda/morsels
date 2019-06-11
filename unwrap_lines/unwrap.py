import re


def unwrap_lines(text):
    return re.sub(r"(?<=[^\n])\n(?=[^\n])", " ", text)
