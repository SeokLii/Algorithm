from collections import Counter

def solution(clothes):
    # 종류마다 나올 수 있는 가지 수에 안 입는 경우의 수를 추가하여 모두 곱함
    # 그리고 모두 안입는 경우의 수를 제거하면 해결 (중요한 해결안)

    kind = [i[1] for i in clothes]

    # nC1(= 종류에 따른 옷 가지수) 구함
    Cou = Counter(kind)
    answer = 1

    # 안입는 경우의 수를 추가하여 모든 값을 곱해서 경우의 수를 구함
    for i in Cou.values():
        answer *= i + 1

    # 모두 안입는 경우 제거
    return answer - 1


# 잘못된 풀이
# 30가지 에대한 조합을 구하게 될 경우 시간 초과가 나게 됨
# 잘못 생각한 부분이 종류마다 나올 수 있는 가지 수를 nC1로 구하고 (=무조건 1개를 뽑는다고 생각)
# 그리고 종류를 뽑는 경우의 수를 구해서 곱해주려고 하였지만 시간 초과
# 종류를 뽑는 경우의 수를 구한 이유는 해당 종류의 옷을 안입는 경우가 있었기 때문이다
# 안뽑는 경우의 수를 추가하여 다 곱해버리면 문제가 가볍게 해결됨
# ex) 얼굴 중 안경, 선글라스(2개) 중 1개를 뽑는 경우의 수가 아닌,, 안쓰는 경우의 수, 안경, 선글라스(3개) 중 1개를 뽑아 버리면 됨
# 그리고 둘 다 안쓰는 경우의 수(1개)를 뺴주면 해결됨
from collections import Counter
from itertools import combinations

def solution(clothes):
    # 종류마다 나올 수 있는 가지 수 nC1로 뽑고 (n= 종류별 개수) (종류별로 하나만 착용이 가능하므로 1)
    # 종류에서 나올 수 있는 가지 수 nC1 + ... + nCr

    # clothes에 하나만 들어있으면 문자열에 대한 Counter가 들어가기 때문에 조건식 대입
    if len(clothes) == 1:
        return 1

    kind = [i[1] for i in clothes]
    Cou = Counter(kind)
    answer = 0
    print(kind, Cou)
    # combinations 함수 이용하는 방법 (조합식 n!/(n-r)!*r! 이용해서 값만 구해줘도 될듯)
    # 종류의 수에 따라 clothes 를 입을 수 있는 조합 선정
    combi = []
    for i in range(1, len(Cou) + 1):
        combi.extend(list(combinations(set(kind), i)))

    # 각 조합에 따라 가지고 있는 의상의 개수를 대입하여 값을 구함
    for i in combi:
        multi = 1
        for j in i:
            multi *= Cou[j]
        answer += multi

    return answer