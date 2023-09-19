sum = 0
while (n := int(input())) > 0:
    sum += n
    if sum > 21:
        print(sum)
        break
else:
    print(n)
