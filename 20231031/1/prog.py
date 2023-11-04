class Omnibus:
    def __setattr__(self, key, value):
        if '_' + key not in self.__dict__:
            setattr(self.__class__,
                    key,
                    self.__class__.__dict__.get(key, 0) + 1)
            self.__dict__['_' + key] = True

    def __getattr__(self, key):
        pass

    def __delattr__(self, key):
        if '_' + key in self.__dict__:
            setattr(self.__class__, key, self.__class__.__dict__[key] - 1)
            if self.__class__.__dict__[key] == 0:
                delattr(self.__class__, key)
            del self.__dict__['_' + key]


import sys
exec(sys.stdin.read())
