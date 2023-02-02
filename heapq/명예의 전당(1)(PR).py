from heapq import *

def solution(k, score):
    answer = []
    heap = []
    heapify(heap)
    for i in range(len(score)):
        heappush(heap, score[i])
        if len(heap) > k:
            heappop(heap)

        answer.append(heap[0])
    return answer