def solution(n, s):
    if s // n < 1:
        return [-1]

    answer = [s // n for i in range(n)]

    for i in range(s % n):
        answer[-1 - i] += 1

    return answer
