class Num:
    def __get__(self, obj, cls):
        if obj is None:
            return self
        return getattr(obj, f"_data_{hex(id(self))}", 0)

    def __set__(self, obj, value):
        _name = f"_data_{hex(id(self))}"
        try:
            setattr(obj, _name, value.real)
        except AttributeError:
            setattr(obj, _name, len(value))


import sys
exec(sys.stdin.read())
