def solution(d, budget):
    answer = 0
    maxn = 0
    d.sort()

    for i in d:
        if maxn + i <= budget:
            answer += 1
            maxn += i
        else:
            break

    return answer