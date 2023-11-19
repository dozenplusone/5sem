class Num:
    def __get__(self, obj, cls):
        return obj.__dict__.setdefault('_data', 0)

    def __set__(self, obj, value):
        try:
            obj._data = value.real
        except AttributeError:
            obj._data = len(value)


import sys
exec(sys.stdin.read())
