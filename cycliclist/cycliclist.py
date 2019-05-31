class CyclicList:
    def __init__(self, iterable):
        self.values = list(iterable)

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return CyclicListIterator(self.values)

    def __getitem__(self, key):
        return self.values[key % len(self.values)]

    def __setitem__(self, key, value):
        self.values[key % len(self.values)] = value

    def append(self, value):
        self.values.append(value)

    def pop(self, key=-1):
        return self.values.pop(key)


class CyclicListIterator:
    def __init__(self, values):
        self.values = values
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.values[self.cursor]
        self.cursor += 1
        if self.cursor >= len(self.values):
            self.cursor = 0

        return res
