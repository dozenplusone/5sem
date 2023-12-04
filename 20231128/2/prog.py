from collections import defaultdict
from math import inf
import sys


vars = defaultdict(float)
ops = {
    "add": float.__add__,
    "sub": float.__sub__,
    "mul": float.__mul__,
    "div": float.__truediv__,
    "ifeq": float.__eq__,
    "ifne": float.__ne__,
    "ifgt": float.__gt__,
    "ifge": float.__ge__,
    "iflt": float.__lt__,
    "ifle": float.__le__
}


def runCmd(cmd):
    match cmd.split():
        case ["stop"]:
            sys.exit(0)
        case ["store", num, var]:
            try:
                vars[var] = float(num)
            except ValueError:
                vars[var] = 0.0
        case ["add" | "sub" | "mul" | "div" as op, src, opd, dest]:
            try:
                vars[dest] = ops[op](vars[src], vars[opd])
            except ZeroDivisionError:
                vars[dest] = inf
        case ["ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle" as cmp,
                src, opd, label]:
            if ops[cmp](vars[src], vars[opd]):
                return label
        case ["out", var]:
            print(vars[var])


labels = {}
cmds = [cmd.strip().split(maxsplit=1) for cmd in sys.stdin.readlines()]
for i, cmd in enumerate(cmds):
    if cmd and cmd[0][-1] == ':':
        labels[cmd[0][:-1]] = i
        cmds[i] = cmd[1]
    else:
        cmds[i] = ' '.join(cmd)
for cmd in cmds:
    match cmd.split():
        case ["ifeq" | "ifne" | "ifgt" | "ifge" | "iflt" | "ifle",
                src, opd, label]:
            if label not in labels:
                sys.exit(1)
i = 0
while i < len(cmds):
    i = labels[label] if (label := runCmd(cmds[i])) is not None else i + 1
