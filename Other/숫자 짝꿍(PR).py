from collections import Counter

def solution(X, Y):
    answer = ''
    CX = Counter(X)
    CY = Counter(Y)

    check = 0
    for i in "9876543210":
        if i in X:
            if i == '0':
                if answer:
                    answer += i * min(CX[i], CY[i])
                else:
                    if min(CX[i], CY[i]) != 0:
                        return '0'
                    else:
                        return '-1'
            else:
                answer += i * min(CX[i], CY[i])

    return answer if answer else '-1'

# 잘못된 풀이
# 만약 Y에 0이 없다면 -1의 결과가 나올 수 없음
# 0일 때에만 -1 처리를 해주었기 때문 그래서 마지막에 return answer을 할때 조건문을 넣어줘야함
from collections import Counter

def solution(X, Y):
    answer = ''
    CX = Counter(X)
    CY = Counter(Y)

    check = 0
    for i in "9876543210":
        if i in X:
            if i == '0':
                if answer:
                    answer += i * min(CX[i], CY[i])
                else:
                    if min(CX[i], CY[i]) != 0:
                        return '0'
                    else:
                        return '-1'
            else:
                answer += i * min(CX[i], CY[i])

    return answer

# 잘못된 풀이
from collections import Counter

def solution(X, Y):
    answer = []
    CX = Counter(X)
    CY = Counter(Y)
    for i in CX:
        if i in CY:
            answer.extend([i * min(CX[i], CY[i])])

    answer.sort(reverse=True)
    return str(int(''.join(answer))) if answer else "-1"