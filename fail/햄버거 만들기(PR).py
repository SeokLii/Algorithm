def solution(ingredient):
    answer = 0
    recipe = [1, 2, 3, 1]
    deq = []
    for i in ingredient:
        deq.append(i)
        while len(deq) >= 4:
            if deq[-4:] != recipe:
                break
            else:
                answer += 1
                for _ in range(4):
                    deq.pop()

    return answer

#잘못된 풀이...
#시간을 단축하기 위해 deque를 썻지만,
# sliceing 하기위해 deque를 list로 변경해주는 과정이 O(n) 만큼 더 많은 시간을 사용하게됨

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