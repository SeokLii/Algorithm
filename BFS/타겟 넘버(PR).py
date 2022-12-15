from itertools import combinations

def solution(numbers, target):
    # 탐색 (경우의 수) == 깊이 너비 탐색
    # 탐색 알고리즘 간의 차이에 대해서 생각해 봐야함
    answer = 0
    SumNumber = sum(numbers)
    for i in range(1, len(numbers)):
        for j in list(combinations(numbers, i)):
            if SumNumber - (2 * sum(j)) == target:
                answer += 1

    return answer