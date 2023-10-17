import timeit

def vow_cons(str):
    tmp = set(str)
    return (len(tmp & set('aeiouy')), len(tmp & set('bcdfghjklmnpqrstvwxz')))

str = input()
loops, time = timeit.Timer(lambda: vow_cons(str)).autorange()
print(loops / time)
