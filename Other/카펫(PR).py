def solution(brown, yellow):
    answer = []
    n = brown + yellow

    # brown + yellow 의 약수를 구한다
    # 그 중 -2 한 값의 곱이 yellow의 개수와 동일한 값이 답
    for i in reversed(range(2, int(n ** 0.5) + 1)):
        if n % i == 0:
            x = i - 2
            y = n // i - 2
            if x * y == yellow:
                answer.append(n // i)
                answer.append(i)

    return answer