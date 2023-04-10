def solution(angle):
    result = angle / 90
    if result < 1:
        return 1
    elif result == 1 :
        return 2
    elif 1 < result < 2:
        return 3
    else:
        return 4