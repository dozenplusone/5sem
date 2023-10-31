class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def __str__(self):
        return "{0}: ({1},{2})({1},{4})({3},{4})({3},{2})".format(
            self.rectcnt,
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )

    def __abs__(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def __lt__(self, obj):
        return abs(self) < abs(obj)

    def __eq__(self, obj):
        return abs(self) == abs(obj)

    def __mul__(self, value):
        return self.__class__(
            value * self.x1,
            value * self.y1,
            value * self.x2,
            value * self.y2
        )

    __rmul__ = __mul__

    def __getitem__(self, value):
        return (
            (self.x1, self.y1),
            (self.x1, self.y2),
            (self.x2, self.y2),
            (self.x2, self.y1)
        )[value]

    def __bool__(self):
        return abs(self) != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
