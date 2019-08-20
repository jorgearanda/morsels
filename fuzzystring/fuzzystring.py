class FuzzyString(str):
    def __eq__(self, other):
        return self.lower() == other.lower()

    def __ne__(self, other):
        return self.lower() != other.lower()

    def __gt__(self, other):
        return self.lower() > other.lower()

    def __ge__(self, other):
        return self.lower() >= other.lower()

    def __lt__(self, other):
        return self.lower() < other.lower()

    def __le__(self, other):
        return self.lower() <= other.lower()

    def __add__(self, other):
        return FuzzyString(str(self) + str(other))

    def __contains__(self, item):
        return item.lower() in self.lower()