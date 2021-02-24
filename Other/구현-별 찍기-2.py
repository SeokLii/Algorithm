import sys

N = int(sys.stdin.readline())

for i in range(N, 0, -1):
    if i == 1:
        print('*'*N)
    else:
        print(' '*(i-2), '*'*(N-(i-1)))