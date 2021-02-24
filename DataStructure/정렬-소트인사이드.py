import sys
N = int(sys.stdin.readline())
List = list(map(int,str(N)))
List.sort(reverse=True)
for i in List:
    print(i, end="")