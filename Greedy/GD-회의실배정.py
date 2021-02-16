def solution(InputArr):
    answer = 0
    endTime = 0
    for i in range(len(InputArr)):
        if endTime <= InputArr[i][0]:
            endTime = InputArr[i][1]
            answer += 1
    return answer


N = int(input())
InputArr = []

for i in range(N):
    A, B = map(int, input().split())
    InputArr.append([A, B])

InputArr.sort(key=lambda x: (x[1], x[0]))
print(solution(InputArr))


# import sys
# from operator import itemgetter
#
# N = int(sys.stdin.readline())
# List = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# List.sort(key=itemgetter(1))
# print(List)

n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: (a[1], a[0]))
#s = sorted(s, key=lambda a: a[1])
print(s)
last = 0
cnt = 0
for i, j in s:
    print(i, j)
    if i >= last:
        print(i, j)
        cnt += 1
        last = j
print(cnt)