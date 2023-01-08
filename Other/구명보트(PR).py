# 정렬 후 투포인트 사용하여 문제풀이
# 최소값과 최대값의 합이 limit 보다 낮으면 투 포인트를 동시에 이동
# 높으면 같이 탈 수 없으므로 start 인덱스만 이동
# 두 포인트가 크로스 체크될 때 break
def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1

    people.sort(reverse=True)
    while True:
        if start > end:
            break
        if people[start] + people[end] <= limit:
            end -= 1

        answer += 1
        start += 1

    return answer


# 잘못된 풀이
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