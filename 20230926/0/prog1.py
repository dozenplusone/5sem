for i in (L := eval(input())):
    if i % 2:
        print(i)
        break
else:
    print(L[-1])