from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(multiplier('1.2', '3.4', float))
print(multiplier('1.2', '3.4', Decimal))
print(multiplier('1/4', '2/3', Fraction))
