from collections import defaultdict

# 중복되는 report는 횟수로 사용하지 않으므로, set을 활용하여 중복값을 제거하여 사용하면 더 빠르게 좋은 값을 가져올 수 있다.
def solution(id_list, report, k):
    answer = []

    stoper = defaultdict(int)  # 정지된 ID
    reporter = defaultdict(list)  # 신고한 ID

    # 신고 중 신고 받은 횟수와 신고한 사람의 목록을 정리
    for i in report:
        p1, p2 = i.split()
        # 동일한 사람이 신고하지 않았다면 (신고하면 이름이 존재)
        if p2 not in reporter[p1]:
            reporter[p1].append(p2)
            stoper[p2] += 1

    # K 회 이상인 경우에만 카운트
    for i in id_list:
        result = 0
        for j in reporter[i]:
            if stoper[j] >= k:
                result += 1
        answer.append(result)

    return answer