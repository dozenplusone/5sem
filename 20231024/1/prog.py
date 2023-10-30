def fib(m, n):
    prev, cur = 0, 1
    for i in range(1, m + 1):
        prev, cur = cur, prev + cur
    for i in range(n):
        yield cur
        prev, cur = cur, prev + cur

import sys
exec(sys.stdin.read())
