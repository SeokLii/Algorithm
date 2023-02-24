from heapq import *

# heapq의 경우 이진트리 형식으로 자동으로 정렬을 해주는데, 이진 트리는 중복 값을 허용하지 않는다
# 그런데 heapq는 허용한다고 하는데, 제대로 정렬되지 않는 모습이 보여졌다.
# 중복 값도 정렬이 되는지 확인이 필요하다
def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K:
        mix = heappop(scoville) + (heappop(scoville) * 2)
        heappush(scoville, mix)
        answer += 1
        if scoville[0] < K and len(scoville) == 1:
            return -1

    return answer



# 잘못된 풀이
def solution(scoville, K):
    answer = 0

    # 오름차순 정렬
    scoville.sort()
    print(scoville)
    # 탐색
    Result = scoville[0]
    for i in range(1, len(scoville)):
        print(Result, scoville[i])
        if Result >= K and scoville[i] >= K:
            return answer
        else:
            Result = min(Result, scoville[i]) + (max(Result, scoville[i]) * 2)
            answer += 1

    # for문을 모두 돌았다면 값이 1개만 남은 상황
    # 1. K가 Result 보다 작을 경우
    # 2. K가 Result 보다 클 경우
    if Result >= K:
        return answer
    else:
        return -1