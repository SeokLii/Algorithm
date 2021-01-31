import sys
N = int(sys.stdin.readline())

F = [0, 1, 3]

for i in range(3, N+1):
    F.append(F[i-1] + (F[i-2]*2))

print(F[N] % 10_007)
