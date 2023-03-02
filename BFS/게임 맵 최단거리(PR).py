# visitor을 안 만들어주고 maps에 메모제이션을 사용하다 보니, maps[0][0] = 1 이어서 한 번 더 0.0이 queue에 들어간다.
def solution(maps):
    N, M = len(maps) - 1, len(maps[0]) - 1
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = [[0, 0]]
    maps[0][0] = 1
    while queue:
        X, Y = queue.pop(0)
        Count = maps[X][Y]
        # finish
        if X == N and Y == M:
            return maps[-1][-1]

        if maps[X][Y] != 0:
            for d in direction:
                x, y = X + d[0], Y + d[1]
                if 0 <= x <= N and 0 <= y <= M:
                    if maps[x][y] == 1:
                        maps[x][y] += Count
                        queue.append([x, y])
    return -1


# 잘못된 풀이
# 메모제이션을 활용하지 않아서, 모든 경로에 대한 최소 값을 구하지 못했음
def solution(maps):
    answer = 0
    N, M = len(maps) - 1, len(maps[0]) - 1
    visitor = maps[:]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = [[0, 0]]
    while queue:
        print(queue)
        X, Y = queue.pop(0)
        # finish
        if X == N and Y == M:
            return answer

        if visitor[X][Y] == 1:
            visitor[X][Y] = 0
            answer += 1
            inp = 0
            for d in direction:
                x, y = X + d[0], Y + d[1]
                if 0 <= x <= N and 0 <= y <= M:
                    if visitor[x][y] == 1:
                        inp += 1
                        queue.append([x, y])

            answer -= (inp - 1)

    print(answer)
    return -1