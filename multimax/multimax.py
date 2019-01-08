def multimax(seq, key=lambda item: item):
    _seq = list(seq)
    max_value = key(max(_seq, key=key, default=None))

    return [item for item in _seq if key(item) == max_value]
