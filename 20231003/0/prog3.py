def funcsum(f, g):
    def h(x):
        return f(x) + g(x)
    return h

xxsqrt = funcsum(lambda x: x ** 2, lambda x: x ** 0.5)
print(xxsqrt(9))
