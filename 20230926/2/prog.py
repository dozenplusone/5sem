lst = list(eval(input()))
len = len(lst)
for i in range(1, len):
    for j in range(len - i):
        if lst[j] ** 2 % 100 > lst[j + 1] ** 2 % 100:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)
