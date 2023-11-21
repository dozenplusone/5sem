import pickle


class SerCls:
    def __init__(self, /, lst=[], dct={}, num=0, st=''):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st


ser = SerCls([42], {13: 37}, 6.9, 'qwerty')
res = pickle.dumps(ser)
del ser
ser1 = pickle.loads(res)
print(ser1.lst, ser1.dct, ser1.num, ser1.st)
