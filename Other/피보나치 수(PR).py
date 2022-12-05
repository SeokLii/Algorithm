def solution(n):
    Fibo = [0, 1]

    for i in range(2, n + 1):
        Fibo.append(Fibo[i - 1] + Fibo[i - 2])
    return Fibo[n] % 1234567