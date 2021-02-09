import sys
T = int(sys.stdin.readline())
A_Rule = [1, -1, 0, 0]
B_Rule = [0, 0, 1, -1]

def setMAP():
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        MAP[Y][X] = 1

def DFS():
    Stack = []
    Stack.append([i, j])
    while Stack:
        A, B = Stack.pop()
        for k in range(4):
            A_sum = A + A_Rule[k]
            B_sum = B + B_Rule[k]
            # 이전코드
            # A += A_Rule
            # B += B_Rule
            # 이렇게 하게 되면 다음 for 문에서 변한 A와 B에 덧셈을 진행하게 되서 틀리게됨
            if 0 <= A_sum < N and 0 <= B_sum < M:
                if MAP[A_sum][B_sum] == 1:
                    Stack.append([A_sum, B_sum])
                    MAP[A_sum][B_sum] = 0

# 전역에 코드를 실행한 거라서 매개변수 없이도 돌아간다.
# 아래 코드를 함수로 묶어주면 매개변수를 다 넣어줘야 한다.
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    MAP = [[0] * M for _ in range(N)]
    Count = 0
    setMAP()
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                continue
            elif MAP[i][j] == 1:
                DFS()
                MAP[i][j] = 0
                Count += 1

    print(Count)

