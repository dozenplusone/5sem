from decimal import Decimal

def esum(N, one):
    ans, cur = type(one)(2), 1
    for i in range(2, N + 1):
        cur *= i
        ans += one / type(one)(cur)
    return ans

N = int(input())
print(esum(N, 1))
print(esum(N, Decimal(1)))
