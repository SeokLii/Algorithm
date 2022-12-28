def solution(m, n, puddles):
    # 하 n, 우 m개로 나올 수 있는 경우의 수를 구하는 것은 시간 복잡도가 높음
    # 해당 경로에 나올 수 있는 경우의 수를 누적으로 더해 가는 것이 맞을 듯
    path = [[0] * m for _ in range(n)]
    path[0][0] = 1

    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] in puddles:
                path[i][j] = 0
            else:
                if i == 0:
                    path[i][j] += path[i][j - 1]
                elif j == 0:
                    path[i][j] += path[i - 1][j]
                else:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]

    return path[n - 1][m - 1] % 1000000007


# 잘못된 문제 풀이
# 가장 바깥 외곽을 1로 설정하고 시작했기 때문에 혹여 웅덩이가 외곽에 있을 경우 문제가 발생
#
def solution(m, n, puddles):
    # 하 n, 우 m개로 나올 수 있는 경우의 수를 구하는 것은 시간 복잡도가 높음
    # 해당 경로에 나올 수 있는 경우의 수를 누적으로 더해 가는 것이 맞을 듯
    path = [[1] * m for _ in range(n)]
    print(path)

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] in puddles:
                path[i][j] = 0
            else:
                path[i][j] = path[i - 1][j] + path[i][j - 1]

    print(path)
    return path[n - 1][m - 1] % 1000000007