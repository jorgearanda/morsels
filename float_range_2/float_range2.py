from math import ceil


class float_range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        (self.start, self.stop, self.step) = (start, stop, step)

    def __len__(self):
        return max(ceil((self.stop - self.start) / self.step), 0)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            new_start = start * self.step + self.start
            new_stop = stop * self.step + self.start
            new_step = step * self.step
            return float_range(new_start, new_stop, new_step)
        if 0 <= index < len(self):
            return self.start + self.step * index
        elif -len(self) <= index < 0:
            return self.start + self.step * (len(self) + index)
        else:
            raise IndexError(f"Index out of range: {index}")
