import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = []
Visited = []
Result = []

R_START = []
B_START = []

X_Rule = [1, -1, 0, 0]
Y_Rule = [0, 0, 1, -1]

for i in range(N):
    TEXT = sys.stdin.readline().rstrip()
    MAP.append(list(TEXT))

    R = TEXT.find('R')
    B = TEXT.find('B')

    if R != -1:
        R_START.append(i)
        R_START.append(R)

    if B != -1:
        B_START.append(i)
        B_START.append(B)

Queue = deque([])
Queue.append(R_START + B_START + [0])
Visited.append(R_START + B_START)

while Queue:
    Location = Queue.popleft()
    for i in range(4):
        R_X = Location[0]
        R_Y = Location[1]
        B_X = Location[2]
        B_Y = Location[3]

        while True:
            if 0 < R_X < N and 0 < R_Y < M-1:  # R 기준으로 움직여서 R의 값을 먼저 높여준다.
                R_X += X_Rule[i]
                R_Y += Y_Rule[i]
                if 0 < B_X < N and 0 < B_Y < M-1:  # R이 가야하지만 B는 그 범위를 넘어간다면 이동을 제한하기 위해 따로 IF문을 만든다.
                    B_X += X_Rule[i]
                    B_Y += Y_Rule[i]

            if MAP[R_X][R_Y] == '.' and MAP[B_X][B_Y] == '#':
                # R을 갈 수 있지만, B는 #으로 막혀서 갈 수 없다면 R만 이동시킨다.
                B_X -= X_Rule[i]
                B_Y -= Y_Rule[i]
            if MAP[B_X][B_Y] == 'O' or MAP[R_X][R_Y] == 'B':
                # R이 B를 만나게 된다면 최소로 진행할 수 없거나, 길이 하나면 O로 B가 먼저 가기때문에 끝낸다.
                # B가 O에 먼저 도착하면 끝낸다.
                break
            if MAP[R_X][R_Y] == '#':  # R 기준으로 진행하기 때문에, R이 #을 만나서 갈 수 없는 경우는 B도 갈 필요가 없다.
                if [R_X-X_Rule[i], R_Y-Y_Rule[i], B_X-X_Rule[i], B_Y-Y_Rule[i]] not in Visited:  # 이전에 갔던 곳이 아니라면
                    Queue.append([R_X-X_Rule[i], R_Y-Y_Rule[i], B_X-X_Rule[i], B_Y-Y_Rule[i], Location[4]+1])
                    Visited.append([R_X-X_Rule[i], R_Y-Y_Rule[i], B_X-X_Rule[i], B_Y-Y_Rule[i]])
                break
            if MAP[R_X][R_Y] == 'O':  # O로 R이 나가고 B는 안나갔을 때 == 정답
                Result.append(Location[4]+1)
                break

R_Len = len(Result)
if R_Len == 0:
    print(-1)
elif R_Len == 1:
    print(Result[0])
else:
    print(min(Result))


# 1. R 기준으로 이동
#
# 2. B 기준으로 이동 B만나면 그냥 끝냄 어짜피 그길은 답이 아니다.
        # R_X = Location[0] + X_Rule[i]
        # R_Y = Location[1] + Y_Rule[i]
        # B_X = Location[2] + X_Rule[i]
        # B_Y = Location[3] + Y_Rule[i]
        # print(i, [R_X, R_Y, B_X, B_Y])
        #
        # while MAP[R_X][R_Y] == '.' and MAP[B_X][B_Y] != 'O':
        #     R_X += X_Rule[i]
        #     R_Y += Y_Rule[i]
        #     B_X += X_Rule[i]
        #     B_Y += Y_Rule[i]
        #     print(i, [R_X, R_Y, B_X, B_Y])





        # if MAP[R_X][R_Y] == '.' and MAP[B_X][B_Y] != 'O':
        #
        #     Queue.append([R_X, R_Y, B_X, B_Y])
        #     MAP[]
        #


# R, B 위치 찾고
# 규칙
# X_Rule = [1, -1, 0, 0]
# Y_Rule = [0, 0, 1, -1]
# R에 대해서만 규칮ㄱ을 적용하고 '.' 로 발견하면 B의 값도 그 값으로 변경(못가면 그자리)
# 만약 B가 먼저 0을 발견하면 배제
# 아니면 그대로 진행하고 result에 저장하고 최소값을 반환