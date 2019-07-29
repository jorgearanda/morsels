def total_length(*seq, use_hints=False):
    res = 0
    for item in seq:
        if use_hints and item.__length_hint__() > 0:
            res += item.__length_hint__()
            continue

        try:
            res += len(item)
        except TypeError:
            res += sum(1 for _ in item)

    return res
