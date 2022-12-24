from itertools import permutations

def solution(numbers):
    answer = 0
    setnum = set()
    for i in range(1, len(numbers) + 1):
        for j in set(permutations(numbers, i)):
            T = int(''.join(j))
            if T > 1:
                setnum.add(T)

    for i in setnum:
        T = 0
        for j in range(1, int(i ** 0.5) + 1):
            if T > 1:
                break
            if i % j == 0:
                T += 1

        if T == 1:
            answer += 1

    return answer