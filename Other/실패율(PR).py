def solution(N, stages):
    answer = []
    player = len(stages)

    for i in range(1, N + 1):
        if player == 0:
            answer.append([i, 0.0])
        else:
            answer.append([i, stages.count(i) / player])
            player -= stages.count(i)

    answer.sort(key=lambda x: -x[1])
    return [answer[i][0] for i in range(len(answer))]