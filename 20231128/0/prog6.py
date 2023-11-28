import inspect


class C:
    a: int

    def __init__(self, val):
        _t = inspect.get_annotations(self.__class__)['a']
        if isinstance(val, _t):
            self.a = val
        else:
            raise TypeError(f"'{_t.__name__}' type required, "
                            + f"got '{type(val).__name__}'")
