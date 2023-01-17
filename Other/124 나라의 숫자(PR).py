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