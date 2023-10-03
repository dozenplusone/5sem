prim_rec = lambda N: 1 + prim_rec(N - 1) if N > 0 else 0

print(prim_rec(10))
