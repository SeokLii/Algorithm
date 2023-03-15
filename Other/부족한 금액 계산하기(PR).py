def solution(price, money, count):
    answer = 0
    for i in range(1, count + 1):
        answer += i * price

    return 0 if answer < money else answer - money