def uniques_only(input):
    """Return an iterable with unique elements from our input."""
    seen = Seen()
    return (elem for elem in input if seen.is_unique(elem))


class Seen:
    """Keep track of seen elements."""
    def __init__(self):
        self._hashables = set()
        self._unhashables = []

    def is_unique(self, value):
        try:
            if value not in self._hashables:
                self._hashables.add(value)
                return True
        except TypeError:
            if value not in self._unhashables:
                self._unhashables.append(value)
                return True

        return False
