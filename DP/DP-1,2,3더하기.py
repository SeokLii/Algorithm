import sys
T = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(T)]
DP = [0, 1, 2, 4]

for i in range(4, 12):
    DP.append(DP[i-1] + DP[i-2] + DP[i-3])

for i in range(T):
    print(DP[N[i]])