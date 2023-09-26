M, N = eval(input())
print([i for i in range(M, N) if not [k for k in range(2, i // 2 + 1) if i % k == 0]])
