def solution(cards):

    # 이중 반복문 사용 (cards < 100)
    # visitor 리스트 생성하여 사용 여부 확인
    visitor = [0 for _ in cards]
    result = []
    for i in range(len(cards)):
        if visitor[i] == 0:
            A = cards[i] -1
            groupnum = 0
            while True:
                if visitor[A] != 0:
                    if groupnum == len(cards):
                        return 0
                    else:
                        result.append(groupnum)
                        break
                else:
                    visitor[A] = 1
                    A = cards[A] -1
                    groupnum += 1

    result.sort(reverse=True)
    return result[0] * result[1]