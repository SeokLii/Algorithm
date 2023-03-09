def solution(keymap, targets):
    answer = []

    for i in targets:
        Csum = 0
        for j in i:
            Cmin = 102
            for k in keymap:
                if j in k:
                    if k.index(j) == 0:
                        Cmin = 1
                        break
                    else:
                        if Cmin > k.index(j) + 1:
                            Cmin = k.index(j) + 1
            if Cmin != 102:
                Csum += Cmin
            else:
                Csum = -1
                break
        answer.append(Csum)

    return answer