from fractions import Fraction as frac

w, h = len(input()) - 2, 0
gas, liquid = 0, 0
while s := input().strip('#'):
    h += 1
    if s[0] == '.':
        gas += w
    else:
        liquid += w
print(
    '#' * (h + 2) + '\n' + \
    ("#" + '.' * h + "#\n") * int(frac(gas, h)) + \
    ("#" + '~' * h + "#\n") * frac(liquid, h).__ceil__() + \
    '#' * (h + 2)
)
pat = "{:<20} {:>" + str(len(str(max(gas, liquid)))) + "}/{}"
if gas < liquid:
    print(pat.format('.' * round(20 * frac(gas, liquid)), gas, gas + liquid))
    print(pat.format('~' * 20, liquid, gas + liquid))
else:
    print(pat.format('.' * 20, gas, gas + liquid))
    print(pat.format('~' * round(20 * frac(liquid, gas)), liquid, gas + liquid))
