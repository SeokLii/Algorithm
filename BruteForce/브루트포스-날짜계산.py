# E : 지구 : 1 ~ 15
# S : 태양 : 1 ~ 28
# M : 달 : 1 ~ 19
E, S, M = map(int, input().split())

standard = 0
result = 0
Cor_S = False
Cor_M = False

while True:
    result = E + standard
    if (result % 28 == 0 and result % 28 + 28 == S) or result % 28 == S:
        Cor_S = True

    if (result % 19 == 0 and result % 19 + 19 == M) or result % 19 == M:
        Cor_M = True

    if Cor_S is True and Cor_M is True:
        break

    Cor_S = False
    Cor_M = False
    standard += 15

print(result)

## 다른 사람이 짠 코드 조금 더 빠르다
# E, S, M = map(int, input().split())
# year = 1
#
# while True:
#     if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
#         print(year)
#         break
#     year += 1