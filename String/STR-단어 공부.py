import sys
Case = sys.stdin.readline().rstrip()

# 대소문자 구분을 안하기 때문에, 대문자로 통일한다.
UpperCase = Case.upper()

# 중복을 제거하여 문자의 종류를 추출한다.
CaseSet = list(set(UpperCase))

CountList = []  # 사용된 횟수 저장하는 리스트

for Kind in CaseSet:
    Count = UpperCase.count(Kind)
    CountList.append(Count)

# CountList에 최대값의 개수가 1보다 크면 == 중복되면
if CountList.count(max(CountList)) > 1: print('?')
else: print(CaseSet[CountList.index(max(CountList))])


# 조건이 살짝 부합하지 못한지 실패가 떳다
# count() 안쓰는게
# import sys
# Case = sys.stdin.readline().rstrip()
#
# # 대소문자 구분을 안하기 때문에, 대문자로 통일한다.
# UpperCase = Case.upper()
# CaseList = list(UpperCase)
#
# # 중복을 제거하여 문자의 종류를 추출한다.
# CaseSet = list(set(UpperCase))
#
# MaxCount = 0  # 사용된 횟수의 최대값
# MaxAlphabet = ''  # 최대로 사용된 알파벳
# Overlap = 0  # 동일한 최대값의 개수
#
# for Kind in CaseSet:
#     Count = 0
#
#     # 사용된 횟수 파악
#     for Alphabet in CaseList:
#         if Kind == Alphabet:
#             Count += 1
#
#     # 최대값 중복 유무 판단 : 가장 많이 사용된 것 표시, 중복되면 끝내기
#     if MaxCount < Count:
#         MaxCount = Count
#         MaxAlphabet = Kind
#     elif MaxCount == Count:
#         print('?')
#         Overlap += 1
#         break
#
# if Overlap == 0:
#     print(MaxAlphabet)


## 설명란 ##
# upper() 대문자로 변환
# lower() 소문자로 변환
# Case의 유래
# 기계 식자가 도입되기 전까지 식자공은 보통 여러 개의 글자를 케이스(cases)라고
# 부르는 상자 한 쌍에 담아 사용했다.
# 소문자는 대문자보다 자주 사용됐기 때문에 식자공과 가까운 아래쪽(lower) 케이스에
# 보관했고, 대문자는 위쪽(upper) 케이스에 보관했다.
# 짐작했겠지만 대문자(upper case)와 소문자(lower case)라는 용어는 두 상자를
# 놓던 자리에서 비롯된 말이다.