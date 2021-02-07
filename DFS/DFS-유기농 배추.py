import sys

T = int(sys.stdin.readline())
Result = []
A_Rule = [1, -1, 0, 0]
B_Rule = [0, 0, 1, -1]

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    MAP = [[0] * N for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        MAP[X][Y] = 1

    Count = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1:
                print(i, j)
                Stack = []
                Stack.append([i, j])
                MAP[i][j] = 0
                Count += 1
                while Stack:
                    A, B = Stack.pop()
                    print(A, B)
                    for i in range(4):
                        print(Stack)
                        A += A_Rule[i]
                        B += B_Rule[i]
                        if 0 <= A < M and 0 <= B < N:
                            if MAP[A][B] == 1:
                                Stack.append([A, B])
                                MAP[A][B] = 0


    Result.append(Count)

for i in Result:
    print(i)
