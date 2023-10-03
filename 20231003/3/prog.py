def Calc(s, t, u):
    def S(x): return eval(s)
    def T(x): return eval(t)
    def U(x, y): return eval(u)
    return lambda x: U(S(x), T(x))

from math import *
print(Calc(*eval(input()))(eval(input())))
