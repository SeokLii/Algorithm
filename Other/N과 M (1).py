from itertools import permutations

M, N = list(map(int, input().split()))
Result = []

for i in range(1, M + 1):
    Result.append(i)

for i in list(permutations(Result, N)):
    for j in range(len(i)):
        print(i[j], end=' ')
    print()
