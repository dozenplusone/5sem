from fractions import Fraction as frac

def issolution(s, w, *args):
    s, w = frac(s), frac(w)
    degA = int(args[0])
    A = frac(args[1])
    for i in range(degA):
        A = s * A + frac(args[2 + i])
    degB = int(args[2 + degA])
    B = frac(args[3 + degA])
    for i in range(degB):
        B = s * B + frac(args[4 + degA + i])
    return B != 0 and A / B == w

print(issolution(*input().split(', ')))
