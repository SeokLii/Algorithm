from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for i in list(permutations(dungeons, len(dungeons))):
        sub_answer = 0
        sub_k = k
        for j in i:
            if j[0] > sub_k:
                continue
            else:
                sub_k -= j[1]
                sub_answer += 1
        if sub_answer > answer:
            answer = sub_answer

    return answer