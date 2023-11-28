class Doubleton(type):
    _instance = [None, None]

    def __call__(cls, *args, **kw):
        ans = cls._instance.pop(0)
        if ans is None:
            ans = super().__call__(*args, **kw)
        cls._instance.append(ans)
        return ans
