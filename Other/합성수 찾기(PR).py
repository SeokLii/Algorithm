def solution(n):
    answer = 0

    for i in range(1, n):
        for j in range(2, int(i ** (0.5))):
            if j % i == 0:
                answer += 1
                break

    return answer