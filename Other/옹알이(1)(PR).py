from itertools import permutations

def solution(babbling):
    kind = []
    for i in range(1, 5):
        kind.extend([''.join(j) for j in list(permutations(["aya", "ye", "woo", "ma"], i))])

    answer = 0
    for i in babbling:
        if i in kind:
            answer += 1
    return answer