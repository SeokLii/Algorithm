def solution(spell, dic):
    answer = 2

    for i in dic:
        sub = list(i)
        if len(sub) == len(set(sub)) and set(sub) == set(spell):
            return 1

    return answer