def solution(number, limit, power):
    answer = 1

    for i in range(2, number + 1):
        gisa = 2
        for j in range(2, int(i ** 0.5) + 1):
            if gisa > limit:
                break
            if i % j == 0:
                if i == j ** 2:
                    gisa += 1
                else:
                    gisa += 2
        if gisa > limit:
            answer += power
        else:
            answer += gisa

    return answer