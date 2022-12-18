from collections import Counter

def solution(k, tangerine):
    answer = 0
    T = Counter(tangerine)

    for i in sorted(T.values(), reverse=True):
        if k > 0:
            k -= i
            answer += 1

    return answer