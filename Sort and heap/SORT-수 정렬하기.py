import sys

N = int(sys.stdin.readline())
List = [int(sys.stdin.readline()) for _ in range(N)]
Sort_List = sorted(List)

for i in Sort_List:
    print(i)