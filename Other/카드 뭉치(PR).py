def solution(cards1, cards2, goal):
    for i in goal:
        if i in cards1:
            if i == cards1[0]:
                cards1.pop(0)
            else:
                return 'No'
        else:
            if i == cards2[0]:
                cards2.pop(0)
            else:
                return 'No'

    return 'Yes'

# 잘못된 풀이
# 모든 카드 정보를 사용한다고 이해하였음, 사용하지 않을 수 도 있으므로 하나씩 확인이 필요
def solution(cards1, cards2, goal):
    sub_goal1 = goal[:]
    sub_goal2 = goal[:]

    for i in cards1:
        if i in sub_goal2:
            sub_goal2.remove(i)
    for i in cards2:
        if i in sub_goal1:
            sub_goal1.remove(i)

    return 'Yes' if sub_goal1 == cards1 and sub_goal2 == cards2 else 'No'

