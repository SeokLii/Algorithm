import sys

N = int(sys.stdin.readline())
List = list(map(int, sys.stdin.readline().split()))
Result = 0

List.sort(reverse=True)
# 오름차순으로 정렬하여 최소값이 가장 많이 겹칠 수 있게 한다.
# 반대로 풀었다.
for i in range(N):
    Result += List[i] * (i+1)

print(Result)
