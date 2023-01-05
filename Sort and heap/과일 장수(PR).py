def solution(k, m, score):
    answer = 0
    if len(score) // m < 1:
        return 0

    score.sort(reverse=True)
    for i in range(len(score) // m):
        answer += score[i * m:(i + 1) * m][-1] * m

    return answer