from math import *

ctr = 0
funcs = {'quit': ['msg', 'msg.format(len(funcs), ctr)']}

def qsplit(s):
    ans = s.split()
    if ans[0][0] != ':'
            and len(funcs[ans[0]]) == 2
            and ans[1][0] in ('"', "'")
            and ans[1][0] == ans[-1][-1]:
        return s.split(maxsplit=1)
    return ans

while s := qsplit(input()):
    ctr += 1
    if s[0][0] == ':':
        funcs[s[0][1:]] = s[1:]
    else:
        print(eval(
            funcs[s[0]][-1],
            globals(),
            {k : eval(v) for k, v in zip(funcs[s[0]][:-1], s[1:])}
        ))
        if s[0] == 'quit':
            break
