from collections import UserString


class DivStr(UserString):
    def __init__(self, value=''):
        super().__init__(value)

    def __floordiv__(self, value):
        L = len(self) // value
        for i in range(value):
            yield self[L*i: L*(i + 1)]

    def __mod__(self, value):
        L = len(self) % value
        return self[-L:] if L else ''


import sys
exec(sys.stdin.read())
