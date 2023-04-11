def solution(babbling):
    answer = 0

    for i in babbling:
        for j in ['aya', 'ye', 'woo', 'ma']:
            if i.count(j * 2) >= 1:
                break
            i = i.replace(j, '*')

        if len(i) == i.count('*'):
            answer += 1

    return answer

# 잘못된 풀이
# 연속된 옹알이를 체크한것이 아니여서 잘못된 풀이
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya', 'ye', 'woo', 'ma']:
            if i.count(j) >= 2:
                break
            i = i.replace(j, '*')

        if len(i) == i.count('*'):
            answer += 1

    return answer