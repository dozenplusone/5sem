n = int(input())
print('A', '+' if n % 50 == 0 else '-', end = ' ')
print('B', '+' if n % 2 and n % 25 == 0 else '-', end = ' ')
print('C', '+' if n % 8 == 0 else '-')
