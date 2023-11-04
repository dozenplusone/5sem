class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1, self.p2, self.p3 = tuple(p1), tuple(p2), tuple(p3)

    def __abs__(self):
        x1, y1, x2, y2, x3, y3 = *self.p1, *self.p2, *self.p3
        ans = 0.5*abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))
        return ans if ans else 0

    def __bool__(self):
        return abs(self) > 0

    def __lt__(self, obj):
        return abs(self) < abs(obj)

    def contains(self, point):
        x1, y1, x2, y2, x3, y3, x0, y0 = *self.p1, *self.p2, *self.p3, *point
        test1 = (x2 - x0)*(y3 - y0) - (x3 - x0)*(y2 - y0)
        test2 = (x3 - x0)*(y1 - y0) - (x1 - x0)*(y3 - y0)
        test3 = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
        return (test1 > 0 and test2 > 0 and test3 > 0
                or test1 < 0 and test2 < 0 and test3 < 0
                or test1 == 0 and min(x2, x3) <= x0 <= max(x2, x3)
                or test2 == 0 and min(x1, x3) <= x0 <= max(x1, x3)
                or test3 == 0 and min(x1, x2) <= x0 <= max(x1, x2))

    def __contains__(self, obj):
        return (not obj
                or (self.contains(obj.p1)
                    and self.contains(obj.p2)
                    and self.contains(obj.p3)))

    def __and__(self, obj):
        return (bool(self) and bool(obj)
                and (self.contains(obj.p1) or obj.contains(self.p1)
                     or self.contains(obj.p2) or obj.contains(self.p2)
                     or self.contains(obj.p3) or obj.contains(self.p3)))


import sys
exec(sys.stdin.read())
