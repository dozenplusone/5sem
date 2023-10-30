import itertools as it
print(*filter(lambda s: s.count('TOR') == 2, (''.join(s) for s in it.product('ORT', repeat=int(input())))), sep=', ')
