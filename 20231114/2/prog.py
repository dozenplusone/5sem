class Num:
    def __get__(self, obj, cls):
        return obj.__dict__.get(f"_data_{hex(id(self))}", 0)

    def __set__(self, obj, value):
        try:
            obj.__dict__[f"_data_{hex(id(self))}"] = value.real
        except AttributeError:
            obj.__dict__[f"_data_{hex(id(self))}"] = len(value)


import sys
exec(sys.stdin.read())
