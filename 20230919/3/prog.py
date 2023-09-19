N = int(input())
i = N
while i <= N + 2:
    j = N
    while j <= N + 2:
        sum = 0
        k = i * j
        while k:
            k, m = divmod(k, 10)
            sum += m
        print(i, '*', j, '=', i * j if sum != 6 else ":=)", end = ' ')
        j += 1
    print()
    i += 1
