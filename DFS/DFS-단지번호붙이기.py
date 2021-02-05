import sys

N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

stack = []
result = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            continue
        if MAP[i][j] == 1:
            stack.append([i, j])
            visited[i][j] = 1
            count = 1
            while stack:
                X, Y = stack.pop()

                if X + 1 < N and visited[X + 1][Y] == 0 and MAP[X + 1][Y] == 1:
                    count += 1
                    visited[X + 1][Y] = 1
                    stack.append([X + 1, Y])

                if X - 1 >= 0 and visited[X - 1][Y] == 0 and MAP[X - 1][Y] == 1:
                    count += 1
                    visited[X - 1][Y] = 1
                    stack.append([X - 1, Y])

                if Y + 1 < N and visited[X][Y + 1] == 0 and MAP[X][Y + 1] == 1:
                    count += 1
                    visited[X][Y + 1] = 1
                    stack.append([X, Y + 1])

                if Y - 1 >= 0 and visited[X][Y - 1] == 0 and MAP[X][Y - 1] == 1:
                    count += 1
                    visited[X][Y - 1] = 1
                    stack.append([X, Y - 1])

            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i)
