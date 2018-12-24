from collections import defaultdict


def default_key_func(item):
    return item


def group_by(seq, key_func=default_key_func):
    res = defaultdict(list)
    for item in seq:
        res[key_func(item)].append(item)

    return res
