def intcheck(func):
    def chk(*args):
        if all(isinstance(arg, int) for arg in args):
            return func(*args)
        else:
            raise TypeError('non-int argument given')
    return chk
