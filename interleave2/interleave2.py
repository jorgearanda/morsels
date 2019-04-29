from itertools import zip_longest


def interleave(*sequences):
    """Interleave sequences of various lengths."""
    skip_me = object()
    interleaved = zip_longest(*sequences, fillvalue=skip_me)
    for group in interleaved:
        for item in group:
            if item is not skip_me:
                yield item
