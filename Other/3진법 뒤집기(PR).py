def solution(n):
    answer = ''
    while n >= 3:
        answer += str(n % 3)
        n //= 3
    answer += str(n)

    # N 진법 -> 10진법 변환 시 int(string, string의 진법) 사용
    return int(answer, 3)