import sys

Expression = sys.stdin.readline().rstrip()
Separation = Expression.split('-')
# 여러 가지수로 묶어보았지만, -를 기준으로 양수의 값을 묶어 음수를 만드는 것이 최소값을
# 가질 수 있는 값이기 때문에 -로만 split 을 해준다.
Result = 0

for i, v in enumerate(Separation):
    Division = list(map(int, v.split('+')))
    if i == 0:  # 첫번째 수는 무조건 양수이기 때문에 더해준다.
        Result += sum(Division)
    else:
        Result -= sum(Division)

print(Result)