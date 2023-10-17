expr = input()
a, b = eval(input())
print(eval(expr, {'x': a, 'y': b}), eval(expr, {'x': b, 'y': a}), sep='\n')
