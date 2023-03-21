def solution(elements):
    answer = set(elements)
    answer.add(sum(elements))
    length = len(elements)
    elements = elements * 2

    for i in range(2, length):
        for j in range(length):
            answer.add(sum(elements[j:j + i]))

    return len(answer)

# 더 빠른 풀이
# 내 풀이는 길이만큼 인덱싱하고 그 합을 집합에 넣어줌
# [7], 9, 1, 1, 4, [7 + 9], 9 + 1, 1 + 1, 1+ 4 ... , [7 + 9 + 1], 9 + 1 + 1,....
# 아래 풀이는 어짜피 리스트의 길이 만큼 값을 다 더하기 때문에 메모제이션하면서 값을 더해줌
# 7 9 1 1 4 에서 [7], [7 + 9], [7 + 9 + 1] 어짜피 해당 인덱스에서 리스트의 길이 만큼 다 더해줄 것이기 때문에 메모제이션을 사용하여 시간을 줄임
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)