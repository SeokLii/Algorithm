def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]

from collections import deque

def solution(n):
    answer = ''
    country = deque()
    while n:
        if n % 3 == 0:
            if country[-1] == '1':
                country.pop()
                country.append(4)
            else:
                country[-1] -= 1
                country.append(4)

        country.append(str(n % 3))
        n //= 3

    answer = list(answer[::-1])
    for i in range(1, len(answer)):
        if answer[i] == '0':
            answer[i - 1] = str(int(answer[i - 1]) - 1)
            answer[i] = '4'

    return str(int(''.join(answer)))

# K진법 구하고 0이 나오는 숫자에 4를 대신 넣어주면 됨
# 결국은 3진법을 구하는 문제
def solution(n):
    answer = ''

    print(n % 3)
    print(n // 3)
    A = []
    n = 12

    while True:
        if n // 3 == 0:
            break

        A.append(n % 3)
        n = n // 3

    A.reverse()
    print(A)
    return answer