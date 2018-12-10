def tail(iterable, elements):
    tail = []
    if elements <= 0:
        return tail

    for item in iterable:
        tail.append(item)
        if len(tail) > elements:
            tail.pop(0)

    return tail
