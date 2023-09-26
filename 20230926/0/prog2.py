A = []
while s := input():
    A.append(list(eval(s)))
if all([len(s) == len(A) for s in A]):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
for s in A:
    print(*s)
