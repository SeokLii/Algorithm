import sys

T = int(sys.stdin.readline())
A_Rule = [1, -1, 0, 0]
B_Rule = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    MAP = [[0] * N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        MAP[X][Y] = 1
    Count = 0
    for i in range(M):
        for j in range(N):
            if MAP[i][j] == 1:
                Stack = []
                Stack.append([i, j])
                MAP[i][j] = 0
                Count += 1
                while Stack:
                    A, B = Stack.pop()
                    for k in range(4):
                        A += A_Rule[k]
                        B += B_Rule[k]
                        if 0 <= A < M and 0 <= B < N:
                            if MAP[A][B] == 1:
                                Stack.append([A, B])
                                MAP[A][B] = 0
    print(Count)

