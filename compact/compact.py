def compact(items):
    """Return an iterator without the adjacent duplicates of its input.

    For example: [1, 2, 2, 3, 1, 1, 2] => [1, 2, 3, 1, 2]
    """
    pristine = True
    for item in items:
        if pristine or item != prev_item:
            yield item
        pristine = False
        prev_item = item
