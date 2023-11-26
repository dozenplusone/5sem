import sys


data = sys.stdin.buffer.read()
N, data = data[0], data[1:]
size = len(data)
data = [data[round(i * size / N): round((i + 1) * size / N)] for i in range(N)]
sys.stdout.buffer.write(bytes((N,)))
for block in sorted(data):
    sys.stdout.buffer.write(bytes(block))
