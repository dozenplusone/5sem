A = []
while s := input():
    A.append(list(eval(s)))
N = len(A) // 2
A, B = A[:N], A[N:]
AB = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            AB[i][k] += A[i][j] * B[j][k]
for row in AB:
    print(*row, sep = ',')
