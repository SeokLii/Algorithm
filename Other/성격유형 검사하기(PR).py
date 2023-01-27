def solution(survey, choices):
    answer = ''
    mbti = {'A': 0, 'N': 0, 'C': 0, 'F': 0, 'M': 0, 'J': 0, 'R': 0, 'T': 0}
    order = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]

    for i in range(len(survey)):
        if choices[i] < 4:
            mbti[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            mbti[survey[i][1]] += choices[i] - 4

    for i in order:
        if mbti[i[0]] < mbti[i[1]]:
            answer += i[1]
        else:
            answer += i[0]

    return answer