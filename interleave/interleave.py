def interleave(iterable1, iterable2):
    for item_from_1, item_from_2 in zip(iterable1, iterable2):
        yield item_from_1
        yield item_from_2
