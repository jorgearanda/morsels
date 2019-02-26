class float_range:
    """Provide elements along a range with float parameters."""

    def __init__(self, first_limit, second_limit=None, step=1):
        if second_limit is None:
            self._start = 0
            self._stop = first_limit
        else:
            self._start = first_limit
            self._stop = second_limit
        self._step = step
        self._cursor = None

    def __len__(self):
        if self._empty_range():
            return 0
        else:
            return int((abs(self._stop - self._start) - 0.00001) // abs(self._step) + 1)

    def __getitem__(self, key):
        if key < len(self):
            return self._start + (key * self._step)
        else:
            raise IndexError

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor is None:
            self._cursor = self._start
        else:
            self._cursor += self._step

        if self._should_stop():
            raise StopIteration
        else:
            return self._cursor

    def _should_stop(self):
        if self._increasing_range():
            return self._reached_top()
        else:
            return self._reached_bottom()

    def _empty_range(self):
        return self._empty_increasing_range() or self._empty_decreasing_range()

    def _empty_increasing_range(self):
        return self._increasing_range() and self._stop <= self._start

    def _empty_decreasing_range(self):
        return not self._increasing_range() and self._start <= self._stop

    def _increasing_range(self):
        return self._step > 0

    def _reached_top(self):
        return self._cursor >= self._stop

    def _reached_bottom(self):
        return self._cursor <= self._stop
