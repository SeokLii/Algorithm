import sys

T = int(sys.stdin.readline())
testcase = [sys.stdin.readline().split() for _ in range(T)]
# 1.거리 탐색: 그래프, 타일
# 2.수 탐색
# 반복해서 찾아야할 규칙을 가지고 있다.
# 중간에 값을 바로 반환하고 싶으면 if 문도 있지만
# 함수를 사용해서 바로 return 탈출 가능
def BFS(i):
    visited = [0 for _ in range(10_000)]
    Queue = []
    Queue.append([i[0], ''])
    visited[int(i[0])] == 1
    while Queue:
        X = Queue.pop(0)
        Number = int(X[0])
        String = X[1]

        D = (Number * 2) % 10_000
        if D == int(i[1]):
            return String + 'D'
        elif visited[D] == 0:
            visited[D] = 1
            Queue.append([D, String + 'D'])

        if Number == 0:
            S = 9999
        else:
            S = Number - 1
        if S == int(i[1]):
            return String + 'S'
        elif visited[S] == 0:
            visited[S] = 1
            Queue.append([S, String + 'S'])

        N_1 = Number // 1000
        N_234 = Number - (N_1 * 1000)
        N_2341 = (N_234 * 10) + N_1
        L = N_2341
        if L == int(i[1]):
            return String + 'L'
        elif visited[L] == 0:
            visited[L] = 1
            Queue.append([L, String + 'L'])

        N_123 = Number // 10
        N_4 = Number - (N_123 * 10)
        N_4123 = (N_4 * 1000) + N_123
        R = N_4123
        if R == i[1]:
            return String + 'R'
        elif visited[R] == 0:
            visited[R] = 1
            Queue.append([R, String + 'R'])

for i in testcase:
    print(BFS(i))


# 시간 초과, 어느 부분에서 시간초과인지 모르겠음