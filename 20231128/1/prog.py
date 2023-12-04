class dump(type):
    def __init__(cls, name, par, ns):
        def makeDump(method):
            def _wrap(self, *args, **kwargs):
                print(method.__name__, ": ", args, ", ", kwargs, sep='')
                return method(self, *args, **kwargs)
            return _wrap

        for method in filter(callable, cls.__dict__.values()):
            setattr(cls, method.__name__, makeDump(method))


import sys
exec(sys.stdin.read())
