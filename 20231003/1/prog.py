def xlty(x, y):
    return x[0] <= y[0] and x[1] <= y[1] and (x[0] < y[0] or x[1] < y[1])

def Pareto(*args):
    ans = []
    for x in args:
        for y in args:
            if xlty(x, y):
                break
        else:
            ans.append(x)
    return tuple(ans)

print(Pareto(*eval(input())))
