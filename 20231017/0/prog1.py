import timeit

print(timeit.Timer(stmt = input()).autorange()[1])
