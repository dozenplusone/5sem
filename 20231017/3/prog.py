from collections import Counter

W = int(input())
countW = Counter()
while s := input().lower():
    countW.update(
        w for w in ''.join(
            c if c.isalpha() else ' ' for c in s
        ).split() if len(w) == W
    )
if countW:
    print(*sorted(
        w for w in countW if countW[w] == max(countW.values(), default = 0)
    ))
