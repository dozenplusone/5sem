def sub(x, y):
    if '__sub__' in dir(x):
        return x - y
    else:
        return type(x)([i for i in x if i not in y])

print(sub(*eval(input())))
