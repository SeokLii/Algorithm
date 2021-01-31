# quotient 몫
# remainder 나머지

import sys

N = int(sys.stdin.readline())

Q5 = N // 5
R5 = N % 5

if R5 % 3 == 0:  # 5로 나눈 나머지가 3의 배수로 나누어떨어지면 5a + 3b로 a+b를 출력
    print(Q5 + (R5 // 3))
else:  # 나누어 떨어지지 않는다면, 5로 나눈 나머지를 3으로 나누면 0, 1, 2 중 하나만 나올 수 있음
    if R5 % 3 == 1 and Q5 >= 1:  # 5로 나눈 나머지를 3으로 나눈 나머지가 1이면
        print((Q5 - 1) + ((R5 // 3) + 2))  # 몫에서 5를 빼서 나머지와 더해 6을 만들고 나눈다
    elif R5 % 3 == 2 and Q5 >= 2:  # 나머지가 2이면
        print((Q5 - 2) + ((R5 // 3) + 4))  # 몫에서 10을 빼서 12를 만들고 3으로 나눈다.
    else:
        print('-1')

# 다른 풀이법
# import sys
# N = int(sys.stdin.readline())
# three = 0
# five = N//5
# N %= 5
# while five >= 0:
#     if N % 3 == 0:
#         three = N//3
#         N %= 3
#         break
#     five -= 1  # 5를 하나씩 올리고 5의 몫에서 -1 하며 나누어떨어질때까지 한다.
#     N += 5
#
# if(N == 0):
#     print(three + five)
# else:
#     print(-1)
