def solution(s):
    answer = []
    sDict = dict()

    for i in range(len(s)):
        if s[i] in sDict:
            answer.append(i - sDict[s[i]])
        else:
            answer.append(-1)
        sDict.update({s[i]: i})

    return answer