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