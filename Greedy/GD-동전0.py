import sys

N, K = map(int, sys.stdin.readline().split())
List = [int(sys.stdin.readline()) for _ in range(N)]
Result = 0

for i in range(N-1, -1, -1):
    Quotient = K // List[i]
    if Quotient == 0:
        continue
    else:
        K = K % List[i]
        Result += Quotient

print(Result)
