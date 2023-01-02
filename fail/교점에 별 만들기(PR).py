from itertools import combinations


def solution(line):
    answer = []

    # 정수의 값을 가지는 별 [X, Y] 값을 구함
    for i in list(combinations(line, 2)):
        AD_BC = i[0][0] * i[1][1] - i[1][0] * i[0][1]
        # 0을 가지면 겹치는 지점이 없다는 의미
        if AD_BC != 0:
            # X
            X = 0
            BF_ED = i[0][1] * i[1][2] - i[1][1] * i[0][2]
            if BF_ED == 0:
                X = 0
            else:
                if BF_ED % AD_BC == 0:
                    X = BF_ED // AD_BC
                else:
                    continue

            # Y
            Y = 0
            EC_AF = i[0][2] * i[1][0] - i[0][0] * i[1][2]
            if EC_AF == 0:
                Y = 0
            else:
                if EC_AF % AD_BC == 0:
                    Y = EC_AF // AD_BC
                else:
                    continue

            answer.append([X, Y])

    # sort 하고 0번째 인덱스값의 양수 값을 더해줌
    sort_X = sorted(answer)
    STX = abs(sort_X[0][0])
    n = 1
    if sort_X[0][0] < 0:
        n += abs(sort_X[0][0])
    if sort_X[-1][0] > 0:
        n += abs(sort_X[-1][0])
    if sort_X[0][0] == sort_X[-1][0]:
        n = 1

    # sort 하고 제일 큰값 빼줘
    # x와 y 값을 반대로 넣어줌
    # 사각형의 n m 값은 최대 최소 abs 더하기 + 1
    sort_Y = sorted(answer, key=lambda x: x[1])
    STY = abs(sort_Y[-1][1]) #여기서 에러 나는 거 같음 (최대 최소 값으로 기준을 다시 잡아야 할듯)
    m = 1
    if sort_Y[0][1] < 0:
        m += abs(sort_Y[0][1])
    if sort_Y[-1][1] > 0:
        m += abs(sort_Y[-1][1])
    if sort_Y[0][1] == sort_Y[-1][1]:
        m = 1

    map = [['.'] * n for _ in range(m)]
    for i in answer:
        map[abs(i[1] - STY)][abs(i[0] + STX)] = '*'

    return [''.join(i) for i in map]