# n = int(input())
# k = 0
# result = 0
# if n % 2 == 1: #홀수
#     result += 1 #세로 방향의 직사각형으로만 이루어진 방법 = 1
#     for i in range(1, n, 2):
#         # 세로 방향의 직사각형이 i
#         # 가로 방향의 직사각형이 차지하는 공간이 n-i
#         F = (n - i) // 2 + i
#         result += F
#
# else: # 짝수
#     result += 2 #세로, 가로 방향으로만 이루어진 방법 = 2
#     for i in range(2, n, 2):
#         # 세로 방향의 직사각형이 i
#         # 가로 방향의 직사각형이 차지하는 공간이 n-i
#         F = (n - i) // 2 + i
#         result += F
#
# print(result)

## 위의 코드는 점화식을 찾으려는 노력보다 그냥 풀려고 해서 틀림
## 점화식을 찾는데 노력을 하자!

# n = int(input())
#
# F = [0 for _ in range(n+1)]
#
# F[1] = 1
# F[2] = 2
# for i in range(3, n+1):
#     F[i] = F[i-1] + F[i-2]
#
# print(F[n]%10007)
## 위에는 런타림 에러

# import sys
# n = int(sys.stdin.readline().rstrip())
#
# F = [0 for _ in range(n+1)]
#
# F[1] = 1
# F[2] = 2
# for i in range(3, n+1):
#     F[i] = F[i-1] + F[i-2]
#
# print(F[n]%10007)
## 위에도 런타임 에러
##그래서 리스트를 만들고 값을 바꿔주는게 아닌 넣어주는 방식으로 바꿈꿈

import sys
n = int(sys.stdin.readline().rstrip())

F = [0, 1, 2]

for i in range(3, n+1):
    F.append(F[i-1] + F[i-2])

print(F[n]%10007)