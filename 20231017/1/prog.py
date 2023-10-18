s = input().lower()
print(len(set(
    x + y for x, y in zip(s[:-1], s[1:]) if x.isalpha() and y.isalpha()
)))
