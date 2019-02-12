import io
import sys


def escape(input):
    with open(input, "rb") as f:
        sys.stdout = io.BytesIO()
        sys.stdout.write(b"print(hello world)")
        sys.stdout.flush()
        # io.BytesIO().write(f.read().decode("utf-8").encode("ascii", "backslashreplace"))


if __name__ == "__main__":
    escape(sys.argv[1])
