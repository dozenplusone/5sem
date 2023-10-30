import itertools as it

def slide(seq, n):
    tees = it.tee(seq)
    i = 0
    while True:
        cur = it.islice(tees[0], i, n + i)
        ans = next(cur, None)
        if ans is None:
            break
        else:
            yield ans
            yield from cur
        tees = it.tee(tees[1])
        i += 1

import sys
exec(sys.stdin.read())
