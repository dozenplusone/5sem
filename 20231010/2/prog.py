from math import *

def fillbrd(a, b):
    return (a + 1, b) if a < b else (b + 1, a)

def scale(a, b, A, B, x):
    return 0.5 * (A + B) if isclose(a, b) else (A + (x - a) * (B - A) / (b - a))

def plot(W, H, a, b, func):
    plt = [[' '] * W for i in range(H)]
    y = [func(scale(0, W - 1, a, b, i)) for i in range(W)]
    w = []
    for i in range(W):
        w.append(j := round(scale(min(y), max(y), H - 1, 0, y[i])))
        plt[j][i] = '*'
    for i in range(W - 1):
        for j in range(*fillbrd(w[i], w[i + 1])):
            plt[j][i] = '*'
    print('\n'.join([''.join(s) for s in plt]))

inp = input().split()
plot(*[eval(s) for s in inp[:-1]], lambda x: eval(inp[-1]))
