from math import *


class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput()
    try:
        ans = 0.5*abs((x3 - x1)*(y2 - y1) - (x2 - x1)*(y3 - y1))
    except Exception:
        raise BadTriangle()
    if isfinite(ans) and ans > 0:
        return ans
    else:
        raise BadTriangle()


while True:
    try:
        ans = triangleSquare(input())
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{ans:.2f}")
        break
