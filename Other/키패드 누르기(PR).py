def solution(numbers, hand):
    answer = ''
    keypade = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    LEFT, RIGHT = [], []

    for i in numbers:
        if i in [1, 4, 7]:  # LEFT
            LEFT.append(keypade[i])
            answer += 'L'
        elif i in [3, 6, 9]:  # RIGHT
            RIGHT.append(keypade[i])
            answer += 'R'

        else:  # 거리 비교
            if len(LEFT) == 0 and len(RIGHT) == 0:
                if hand == 'right':
                    RIGHT.append(keypade[i])
                    answer += 'R'
                else:
                    LEFT.append(keypade[i])
                    answer += 'L'
            elif len(LEFT) == 0:
                if abs(keypade[i][0] - RIGHT[-1][0]) + abs(keypade[i][1] - RIGHT[-1][1]) > 1:
                    LEFT.append(keypade[i])
                    answer += 'L'
                else:
                    RIGHT.append(keypade[i])
                    answer += 'R'
            elif len(RIGHT) == 0:
                if abs(keypade[i][0] - LEFT[-1][0]) + abs(keypade[i][1] - LEFT[-1][1]) > 1:
                    RIGHT.append(keypade[i])
                    answer += 'R'
                else:
                    LEFT.append(keypade[i])
                    answer += 'L'
            else:
                LeftD = abs(keypade[i][0] - LEFT[-1][0]) + abs(keypade[i][1] - LEFT[-1][1])
                RightD = abs(keypade[i][0] - RIGHT[-1][0]) + abs(keypade[i][1] - RIGHT[-1][1])
                if LeftD == RightD:
                    if hand == 'right':
                        RIGHT.append(keypade[i])
                        answer += 'R'
                    else:
                        LEFT.append(keypade[i])
                        answer += 'L'
                elif LeftD > RightD:
                    RIGHT.append(keypade[i])
                    answer += 'R'
                else:
                    LEFT.append(keypade[i])
                    answer += 'L'

    return answer
