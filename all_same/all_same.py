from collections.abc import Hashable


def all_same(seq):
    first_item = uninitialized = object()
    for item in seq:
        hashed_item = _get_hashed(item)
        if first_item == uninitialized:
            first_item = hashed_item
        if first_item != hashed_item:
            return False

    return True


def _get_hashed(item):
    if isinstance(item, Hashable):
        return hash(item)
    elif isinstance(item, list):
        return hash(tuple(item))
    else:
        return hash(tuple(sorted(item.items())))
