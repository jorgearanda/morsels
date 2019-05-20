from collections.abc import Iterable


def deep_flatten(input):
    for element in input:
        if isinstance(element, Iterable) and type(element) is not str:
            yield from deep_flatten(element)
        else:
            yield element
