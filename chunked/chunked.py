from itertools import islice, zip_longest

sentinel = object()


def chunked(seq, size, *, fill=sentinel):
    if fill == sentinel:
        it = iter(seq)
        return iter(lambda: tuple(islice(it, size)), ())
    else:
        args = [iter(seq)] * size
        return zip_longest(fillvalue=fill, *args)
