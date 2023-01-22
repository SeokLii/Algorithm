from heapq import *


def solution(operations):
    answer = []
    heapify(answer)
    check = 0
    for i in operations:
        if i[0] == 'D' and check == 0:
            continue
        else:
            if i[0] == 'I':
                heappush(answer, int(i[2:]))
                check += 1
            elif i[0] == 'D' and i[2] == '-':
                heappop(answer)
                check -= 1
            else:
                answer.pop()
                check -= 1

    if len(answer) == 0:
        return [0, 0]
    else:
        return [max(answer), min(answer)]