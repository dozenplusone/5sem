from string import ascii_lowercase


class Alpha:
    __slots__ = tuple(ascii_lowercase)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        ans = ''
        for slot in self.__slots__:
            try:
                ans += slot + ": " + repr(getattr(self, slot)) + ", "
            except AttributeError:
                pass
        return ans[:-2]


class AlphaQ:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __setattr__(self, key, value):
        if len(key) != 1 or key not in ascii_lowercase:
            raise AttributeError
        self.__dict__[key] = value

    def __str__(self):
        ans = ''
        for k, v in sorted(self.__dict__.items()):
            ans += k + ": " + repr(v) + ", "
        return ans[:-2]


import sys
exec(sys.stdin.read())
