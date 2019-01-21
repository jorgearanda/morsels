def multimax(seq, key=lambda item: item):
    """Return all the items in a sequence that are the maximum value of the sequence."""
    max_value = None
    res = []
    for value in seq:
        if max_value is None or max_value == key(value):
            max_value = key(value)
            res.append(value)
        elif max_value < key(value):
            max_value = key(value)
            res = [value]

    return res
