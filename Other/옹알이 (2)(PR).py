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