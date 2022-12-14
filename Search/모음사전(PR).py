from itertools import product

def solution(word):
    vowel = ['AEIOU']
    lib = []

    # vowel에 대한 n개의 가지수를 모두 구해서 넣어줌
    for i in range(1, 6):
        lib += [''.join(i) for i in list(product(*vowel, repeat=i))]

    # sort 하면 사전 순으로 정렬됨
    lib.sort()

    return lib.index(word) + 1