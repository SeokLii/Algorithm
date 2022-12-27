visit = []


def solution(n, computers):
    global visit
    visit = [0 for i in range(n)]
    answer = 0

    while True:
        try:
            idx = visit.index(0)
            dfs(idx, n, computers)
            answer += 1
        except:
            break

    return answer


def dfs(idx, n, computers):
    global visit
    visit[idx] = 1
    for i in range(n):
        if visit[i] == 0 and computers[idx][i] == 1:
            dfs(i, n, computers)