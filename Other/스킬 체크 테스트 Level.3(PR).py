def solution(n, s):
    if s // n == 0:
        return [-1]
    else:
        answer = [s // n for i in range(n)]
        for i in range(s % n):
            answer[-1 - i] += 1
    return answer

# 징검다리 건너기 이분 탐색 풀이
def solution(stones, k):
    left, right = min(stones), max(stones)
    while left <= right:
        temp = stones[:]
        mid = (left + right) // 2
        cnt = 0
        for t in temp:
            if t - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1

    return left