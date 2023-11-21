import sys


with open(sys.argv[1], 'rt') as f:
    data = f.read()

stop = len(data) // 3
print(data[:stop] + data[stop: data.find('\n', stop)])
