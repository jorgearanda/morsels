def all_same(seq):
    first_item = next(iter(seq), None)
    return all(
        item == first_item
        for item in seq
    )
