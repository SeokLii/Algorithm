def solution(park, routes):
    start = []
    n, m = len(park[0]) - 1, len(park) - 1
    for i in range(len(park)):
        if 'S' in park[i]:
            start = [i, park[i].index('S')]
            break

    for i in routes:
        if i[0] == 'E':
            if start[1] + int(i[2]) <= n:
                check = 0
                for j in range(1, int(i[2]) + 1):
                    if park[start[0]][start[1] + j] == 'X':
                        check = 1
                        break
                if check == 1:
                    continue
                start[1] += int(i[2])
        elif i[0] == 'W':
            if start[1] - int(i[2]) >= 0:
                check = 0
                for j in range(1, int(i[2]) + 1):
                    if park[start[0]][start[1] - j] == 'X':
                        check = 1
                        break
                if check == 1:
                    continue
                start[1] -= int(i[2])
        elif i[0] == 'S':
            if start[0] + int(i[2]) <= m:
                check = 0
                for j in range(1, int(i[2]) + 1):
                    if park[start[0] + j][start[1]] == 'X':
                        check = 1
                        break
                if check == 1:
                    continue
                start[0] += int(i[2])
        else:
            if start[0] - int(i[2]) >= 0:
                check = 0
                for j in range(1, int(i[2]) + 1):
                    if park[start[0] - j][start[1]] == 'X':
                        check = 1
                        break
                if check == 1:
                    continue
                start[0] -= int(i[2])

    return start