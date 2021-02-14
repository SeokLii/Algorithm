import sys

N = int(sys.stdin.readline())
Weight_List = [int(sys.stdin.readline()) for _ in range(N)]
Weight_List.sort(reverse=True)
Result = 0
# 무게가 20KG이고 루프가 2개일 경우 각 루프는 W/k 이기 때문에 10키로의 중량을 나눠가진다.
# 무게가 22KG이면 각 루프가 11키로의 중량을 나눠가지지만 한 루프는 10키로 밖에 들 수 없기 때문에
# 불가능하다.
# 또한 10, 15일 경우 10, 10을 버틸 수는 있지만 15, 15는 불가능 하기 때문에
# 내림차순으로 각 루프를 정렬하고 15를 1개 쓰는 경우와
# 10 10으로 2개를 쓰는 경우로 나누어서 구할 수가 있다.
# 다른 예시로는 [10, 5, 20, 17]일 경우 [20, 17, 10 5]로 내림차순 정렬이 가능하고
# 20인 경우는 20 1개, 17인 경우는 20이 17의 무게도 견딜 수 있으므로 17 2개가 가능하다
# 10일 경우는 3개 ....
# list(n) * n+1 로 반복해 가면서 풀 수 있다. 또한 GD인 만큼 정렬이 중요하다.

for i, v in enumerate(Weight_List):
    MAX = v * (i+1)
    if MAX > Result:
        Result = MAX

print(Result)