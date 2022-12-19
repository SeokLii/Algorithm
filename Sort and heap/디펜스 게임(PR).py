from heapq import *

# 첫번째 해결안
# 매번 리스트를 인덱싱해서 자르고 해당 값들 중 최대값을 제거하여(sort 사용하여) 최소값읋 구하다보니 복잡해지고 시간초과됨
def solution(n, k, enemy):
    Length = len(enemy)

    # 무적권이 더 많다면 enemy 길이만큼 반환
    if Length <= k:
        return Length
    else:
        # k+1부터 Length - k 길이만큼 리스트를 인덱싱
        sub_enemy = enemy[:k]
        heapify(sub_enemy)
        for i in range(k, Length):
            # 최대값을 무적권으로 제거해야 더 많은 라운드를 막을 수 있다는 최적의 해가 존재하므로
            # 오름차순 정렬 후 왼쪽부터(작은 값들) 무적권을 제거한 개수들의 합이 n을 넘는지 확인
            # 매번 enemy를 인덱싱할 수 없으므로 heapq 이용
            heappush(sub_enemy, enemy[i])
            sub_sum = sum(sub_enemy[:-k])
            print(sub_enemy, sub_enemy[:-k])

            if sub_sum > n:
                return len(sub_enemy) - 1
            elif sub_sum == n:
                return len(sub_enemy)

# 두번째 해결안
# 최소 최대 값에 대한 추가 또는 삭제를 진행 할 때 자동으로 sort하여 저장해주기 때문에 시간이 덜 들고
# 구조적으로 따로 min 또는 max를 구할 필요가 없어서 훨씬 빠르게 동작함
def solution(n, k, enemy):
    heap = []
    total = round_ = 0
    for each in enemy:
        total += each
        if total <= n:
            heappush(heap, -each)
            round_ += 1
        elif k > 0:
            k -= 1
            total += heappushpop(heap, -each)
            round_ += 1
        else:
            break
    return round_

# 세번째 해결안
import heapq as hq
def solution(n, k, enemy):
    q = enemy[:k]
    hq.heapify(q)
    for idx in range(k,len(enemy)):
        n -= hq.heappushpop(q,enemy[idx])
        if n < 0:
            return idx
    return len(enemy)