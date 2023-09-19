while str := input():
    if str == '13':
        break
    if int(str) % 2 == 0:
        print(str)
else:
    print('No 13!')
