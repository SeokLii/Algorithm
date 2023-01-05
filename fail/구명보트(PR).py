from collections import deque

def solution(people, limit):
    answer = 0
    A = deque(people)
    P = 0

    while True:
        if len(A) <= 1:
            break
        else:
            if A[0] > limit // 2:
                A.popleft()
            else:
                other = limit - A[0]
                if other in A:
                    A.popleft()
                    A.remove(other)
                    P += 1
                else:
                    A.popleft()

    print(P)
    return answer