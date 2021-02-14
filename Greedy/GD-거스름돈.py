import sys

money_list = [500, 100, 50, 10, 5, 1]  # 해당 규칙에 대해서 정렬이 필요하다.
pay = int(sys.stdin.readline())
change = 1000 - pay
result = 0

for i in money_list:
    Quotient = change // i
    if Quotient > 0:
        result += Quotient
        change = change % i

print(result)