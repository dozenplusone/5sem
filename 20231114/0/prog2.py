def typecheck(type):
    def checker(func):
        def chk(*args):
            if all(isinstance(arg, type) for arg in args):
                return func(*args)
            else:
                raise TypeError(f'non-{type.__name__} argument given')
        return chk
    return checker
