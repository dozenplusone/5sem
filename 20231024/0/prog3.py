def travel(n):
    for i in range(n):
        yield "по кочкам"
    else:
        return "и в яму"

def travelwrap(n):
    ans = yield from travel(n)
    yield ans
