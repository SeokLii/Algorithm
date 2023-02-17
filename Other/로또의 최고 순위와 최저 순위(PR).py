def solution(lottos, win_nums):
    corr = 0
    zero = 0
    for i in lottos:
        if i == 0:
            zero += 1
        else:
            if i in win_nums:
                corr += 1

    if corr == 0 and zero == 0:
        corr = 1
    elif corr == 0:
        corr = 1
        zero -= 1

    return [7 - (zero + corr), 7 - corr]


# 깔끔한 다른 사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]