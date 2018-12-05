from math import pi


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0

    @property
    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return f'Circle({self.radius})'
