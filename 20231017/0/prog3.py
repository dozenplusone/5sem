from collections import Counter
import timeit

def wordsDic(str):
    dic = {}
    for word in str.split():
        dic[word] = dic.setdefault(word, 0) + 1
    return dic

def wordsCounter(str):
    return Counter(str.split())

str = input()
loopsDic, timeDic = timeit.Timer(lambda: wordsDic(str)).autorange()
loopsCounter, timeCounter = timeit.Timer(lambda: wordsCounter(str)).autorange()
print('wordsDic     =', loopsDic / timeDic)
print('wordsCounter =', loopsCounter / timeCounter)
print(*wordsCounter(str).keys())
