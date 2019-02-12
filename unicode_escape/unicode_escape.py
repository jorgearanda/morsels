import unicodedata
import sys


def escape(input):
    with open(input, "r") as f:
        print(f.read().encode("raw_unicode_escape").decode(), end="")


if __name__ == "__main__":
    escape(sys.argv[1])
