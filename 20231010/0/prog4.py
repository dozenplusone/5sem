from math import sin

def scale(a, b, A, B, x):
    return A + (x - a) * (B - A) / (b - a)

W, H, A, B = eval(input())
for i in range(H):
    x = scale(0, H - 1, A, B, i)
    print(' ' * int(scale(-1, 1, 0, W - 1, sin(x))), '*')
