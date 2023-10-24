from itertools import product

print(*(''.join(i) for i in product('abcdefgh', '12345678')))
