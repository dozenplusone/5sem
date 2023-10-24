def invsqs():
    ans = 1
    i = 1
    while True:
        yield ans
        i += 2*i + 1
        ans += 1 / i

print(sum(1 / i**2 for i in range(1, 10001)))
