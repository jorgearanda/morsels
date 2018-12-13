from collections import deque


def tail(iterable, elements):
    if elements <= 0:
        return []
    return list(deque(iterable, maxlen=elements))
