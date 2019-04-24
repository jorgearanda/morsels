class PermaDict(dict):
    def __init__(self, *args, **kwargs):
        if "silent" in kwargs:
            self.silent = kwargs["silent"]
            del kwargs["silent"]
        else:
            self.silent = False
        super().update(*args, **kwargs)

    def __setitem__(self, key, value, force_set=False):
        if key in self:
            if self.silent is True:
                return
            else:
                raise KeyError
        super().__setitem__(key, value)

    def update(self, *args, **kwargs):
        if "force" in kwargs:
            del kwargs["force"]
            super().update(*args, **kwargs)
        else:
            for key, value in dict(*args, **kwargs).items():
                self[key] = value

    def force_set(self, key, value):
        super().__setitem__(key, value)
