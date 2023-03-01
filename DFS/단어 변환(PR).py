from collections import defaultdict

# DFS에 필요한 데이터를 직접 생성하고, DFS를 진행하는 문제
def solution(begin, target, words):
    # words 데이터 간의 연결 리스트 생성
    Ldic = defaultdict(list)
    words.append(begin)
    for i in words:
        for j in words:
            check = 0
            for n in range(len(j)):
                if i[n] == j[n]:
                    check += 1
            if check == len(j) - 1:
                Ldic[i].append(j)

    # DFS
    answer = - 1
    visitor = []
    stack = [begin]

    while stack:
        check = 0
        answer += 1
        q = stack.pop()
        if q == target:
            return answer

        if q not in visitor:
            visitor.append(q)
            for i in Ldic[q]:
                if i not in visitor:
                    check += 1
                    stack.append(i)
            if check == 0:
                answer -= 1

    return 0

# 잘못된 풀이
def solution(begin, target, words):
    answer = 1
    queue = [begin]

    print(queue)
    while queue:
        if queue[0] == target:
            return answer
        for i in range(len(queue[0])):
            if queue[0][i] != target[i]:
                sub = queue[0][:i] + target[i] + queue[0][i + 1:]
                print(sub)
                if sub in words:
                    print(sub)
                    queue.append(sub)
        print(queue)
        queue.pop(0)
        answer += 1

    print(queue)
    return 0

# 잘못된 풀이
answer = 0

def solution(begin, target, words):
    global answer
    try:
        words.index(target)
        answer = 4
        return answer
    except:
        return answer


def dfs(start, begin_list, target, words):
    global answer
    begin_list[start] = 'c'
    answer = 3
    print(begin_list)
    print('daw', words.index(''.join(begin_list)))
    # try:
    #     idx = words.index(''.join(begin_list))
    #     del words[idx]
    #     answer += 1
    #     print(answer)
    #     dfs(start+1, begin_list, target, words)
    # except:
    #     return answer
    #     print('d')