from collections import deque


def solution(ingredient):
    answer = 0
    recipe = [1, 2, 3, 1]
    deq = deque()
    for i in ingredient:
        deq.append(i)
        while len(deq) >= 4:
            if list(deq)[-4:] != recipe:
                break
            else:
                answer += 1
                for _ in range(4):
                    deq.pop()

    return answer