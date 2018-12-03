from math import pi


class Circle:
    def __init__(self, radius=1.0):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2.0

    @property
    def area(self):
        return pi * self._radius ** 2

    def __repr__(self):
        return f'Circle({self.radius})'

    def __str__(self):
        return f'Circle({self.radius})'
