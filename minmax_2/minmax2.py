from collections import namedtuple
from itertools import tee

guard = object()
MinMax = namedtuple("MinMax", ["min", "max"])


def minmax(seq, *, key=lambda x: x, default=guard):
    try:
        iter1, iter2 = tee(seq)
        return MinMax(min(iter1, key=key), max(iter2, key=key))
    except ValueError:
        if default is not guard:
            return MinMax(default, default)
        else:
            raise ValueError("minmax() arg is an empty iterable")
