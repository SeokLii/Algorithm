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