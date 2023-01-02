
## 잘못된 풀이
from collections import deque

def solution(info, query):
    answer = deque()
    # info 파싱
    info = [i.split() for i in info]

    # query 파싱
    query = [i.replace(' and ', ' ').split() for i in query]

    # 검색
    # 효율이 안나와서 fail
    # 딕셔너리를 이용해야함
    for q in query:
        search = 0
        for i in info:
            check = 0
            if int(q[4]) > int(i[4]):
                continue
            else:
                for k in range(4):
                    if q[k] == '-' or q[k] == i[k]:
                        check += 1
                    else:
                        break
            if check == 4:
                search += 1
        answer.append(search)

    return list(answer)