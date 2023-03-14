from itertools import combinations

def solution(nums):
    answer = 0
    for i in list(combinations(nums, 3)):
        answer += 1
        checknum = sum(i)
        for j in range(2, int(checknum**(0.5)) + 1):
            if checknum % j == 0:
                answer -= 1
                break

    return answer