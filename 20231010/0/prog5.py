from math import sin

def scale(a, b, A, B, x):
    return A + (x - a) * (B - A) / (b - a)

W, H, A, B = eval(input())
scr = [[' '] * W for i in range(H)]
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    scr[int(scale(-1, 1, H - 1, 0, sin(x)))][i] = '*'
print('\n'.join([''.join(s) for s in scr]))
