from collections import Iterable


def deep_add(input, start=0):
    """Add the leaf elements in a nested iterable."""
    total = None
    for element in _flatten(input):
        if total is None:
            total = element
        else:
            total += element
    if total is None:
        return start
    else:
        return start + total


def _flatten(input):
    for element in input:
        if isinstance(element, Iterable):
            yield from _flatten(element)
        else:
            yield element
