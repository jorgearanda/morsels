class alias():
    def __init__(self, name, write=False):
        self.name = name
        self.write = write

    def __get__(self, obj, cls):
        if obj is not None:
            return getattr(obj, self.name)
        elif cls is not None:
            return getattr(cls, self.name)
        else:
            return self

    def __set__(self, obj, val):
        if self.write:
            setattr(obj, self.name, val)
        else:
            raise AttributeError("can't set attribute")
