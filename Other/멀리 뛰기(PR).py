def solution(n):
    # 경우의 수, 조합의 경우 = 결과에서 규칙 존재 확률이 높음(= 피보나치 수와 비슷)

    Lfibo = [1, 1]
    for i in range(2, n + 1):
        Lfibo.append(Lfibo[i - 1] + Lfibo[i - 2])

    return Lfibo[n] % 1234567
