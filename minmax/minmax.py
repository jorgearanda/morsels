from collections import namedtuple
from itertools import tee

MinMax = namedtuple("MinMax", ["min", "max"])


def minmax(seq, *, key=lambda x: x):
    """Return the minimum and maximum values in the input."""
    iterator1, iterator2 = tee(seq)

    return MinMax(min(iterator1, key=key), max(iterator2, key=key))
