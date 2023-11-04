open, close = '\u00b7', '\u2588'


class Maze:
    def __init__(self, value):
        self.maze = [[close] * (2*value + 1) for i in range(2*value + 1)]
        for i in range(1, 2*value, 2):
            self.maze[i][1::2] = open * value

    def __str__(self):
        return '\n'.join(''.join(s) for s in self.maze)

    def __getitem__(self, key):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        check = [len(self.maze)//2 * [0] for i in range(len(self.maze)//2)]
        step = 1
        plan = [(y0, x0)]
        check[y0][x0] = step
        while plan:
            step += 1
            cur = plan.pop()
            check[cur[0]][cur[1]] = step
            if self.maze[2*cur[0] + 1][2*cur[1]] == open:
                if cur[0] == y1 and cur[1] - 1 == x1:
                    return True
                if check[cur[0]][cur[1] - 1] == 0:
                    plan += [(cur[0], cur[1] - 1)]
            if self.maze[2*cur[0] + 1][2*(cur[1] + 1)] == open:
                if cur[0] == y1 and cur[1] + 1 == x1:
                    return True
                if check[cur[0]][cur[1] + 1] == 0:
                    plan += [(cur[0], cur[1] + 1)]
            if self.maze[2*cur[0]][2*cur[1] + 1] == open:
                if cur[0] - 1 == y1 and cur[1] == x1:
                    return True
                if check[cur[0] - 1][cur[1]] == 0:
                    plan += [(cur[0] - 1, cur[1])]
            if self.maze[2*(cur[0] + 1)][2*cur[1] + 1] == open:
                if cur[0] + 1 == y1 and cur[1] == x1:
                    return True
                if check[cur[0] + 1][cur[1]] == 0:
                    plan += [(cur[0] + 1, cur[1])]
        return check[y1][x1] > 0

    def __setitem__(self, key, value):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        if x0 == x1:
            y0, y1 = min(y0, y1), max(y0, y1)
            x0 = 2*x0 + 1
            for i in range(2*(y0 + 1), 2*y1 + 1, 2):
                self.maze[i][x0] = value
        elif y0 == y1:
            x0, x1 = min(x0, x1), max(x0, x1)
            y0 = 2*y0 + 1
            for i in range(2*(x0 + 1), 2*x1 + 1, 2):
                self.maze[y0][i] = value


import sys
exec(sys.stdin.read())
