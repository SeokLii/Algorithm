from collections import Counter

def solution(str1, str2):
    # 대문자로 변환
    str1 = str1.upper()
    str2 = str2.upper()

    # 문자열 파싱
    str1_list = []
    str2_list = []
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUWXYVZ'

    for i in range(len(str1) - 1):
        if str1[i] in Alphabet and str1[i + 1] in Alphabet:
            str1_list.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i] in Alphabet and str2[i + 1] in Alphabet:
            str2_list.append(str2[i:i + 2])

    # 다중 집합인지 확인
    str1_set = set(str1_list)
    str2_set = set(str2_list)
    J = 0
    if len(str1_list) == len(str1_set) and len(str2_list) == len(str2_set):
        # 다중 집합이 아니면 바로 교집합 및 합집합의 길이 구하기
        if len(str1_set) == 0 and len(str2_set) == 0:
            return 65536
        else:
            union = len(str1_set | str2_set)
            intersection = len(str1_set & str2_set)
            J = intersection / union
    else:
        # 다중 집합이면
        # Counter 안쓰고, set 값을 count 해서 중복 값이 존재하면
        # 해당 값의 max or min값을 추가로 넣어주었으면 더 좋은 방법이 되었을 듯
        str1_counter = Counter(str1_list)
        str2_counter = Counter(str2_list)
        union = 0
        intersection = 0

        for key, val in str1_counter.items():
            if key in str2_counter.keys():
                union += max(val, str2_counter[key])
                intersection += min(val, str2_counter[key])
            else:
                union += val

        for key, val in str2_counter.items():
            if key not in str1_counter.keys():
                union += val

        J = intersection / union

    # 65536을 곱하고 정수형으로 변환
    return int(J * 65536)