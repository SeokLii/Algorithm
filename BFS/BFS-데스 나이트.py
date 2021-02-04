import sys

N = int(sys.stdin.readline())
r_start, c_start, r_finish, c_finish = map(int,sys.stdin.readline().split())
# **split() 자체가 리스트로 반환한다**

# N X N 체스판
visited = [[0] * N for _ in range(N)]
# model = [[0] * N for _ in range(N)]
# 이번에는 model 과 visited 가 같이 사용되지 않았다.
# 여러 경우에 대해서 주의해야한다.

rule = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
# 대신에 규칙이 따로 존재해서 만들어서 사용했다.
# while 문 안에서 반복해야하는 규칙을 잘 살펴야한다.

Queue = []
Queue.append([r_start, c_start])
visited[r_start][c_start] = 0

while Queue:
    X = Queue.pop(0)
    for i in rule:
        r = X[0] + i[0]
        c = X[1] + i[1]
        if (-1 < r < N and -1 < c < N) and (visited[r][c] == 0 or visited[r][c] > visited[X[0]][X[1]] + 1):
            # 방문하지 않았거나 방문했다면 방문 횟수의 최소값을 넣어줘야 한다는 if 문을 꼭 넣어줘야 한다.
            Queue.append([r, c])
            visited[r][c] = visited[X[0]][X[1]] + 1

print(visited[r_finish][c_finish] if visited[r_finish][c_finish] != 0 else -1)