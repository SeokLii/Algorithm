def solution(n, m, section):
    answer = 0
    point = 0
    for i in section:
        if i > point:
            point = i + m - 1
            answer += 1
    return answer