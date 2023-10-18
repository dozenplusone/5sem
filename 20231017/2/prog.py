from math import *

def qsplit(s):
    s += ' '
    qt = ''
    ans = []
    last = 0
    for i in range(len(s)):
        if not qt and s[i].isspace():
            if last != i:
                ans.append(s[last : i])
            last = i + 1
        elif not qt and s[i] in ("'", '"'):
            qt = s[i]
        elif s[i] == qt:
            qt = ''
    return ans

ctr = 0
funcs = {'quit': ['msg', 'msg.format(len(funcs), ctr)']}

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
