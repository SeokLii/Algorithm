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