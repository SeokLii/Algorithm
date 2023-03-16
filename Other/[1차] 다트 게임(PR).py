def solution(dartResult):
    answer = []
    Number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    Bonus = {'S': 1, 'D': 2, 'T': 3}
    for i in range(len(dartResult)):
        if dartResult[i] == '0' and dartResult[i - 1] == '1':
            continue

        if dartResult[i] in Number:
            if dartResult[i] == '1' and dartResult[i + 1] == '0':
                answer.append(10)
            else:
                answer.append(int(dartResult[i]))
        else:
            if dartResult[i] in Bonus:
                answer[-1] = answer[-1] ** Bonus[dartResult[i]]
            elif dartResult[i] == "*":
                if len(answer) < 2:
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2
                    answer[-2] *= 2
            else:
                answer[-1] = -answer[-1]

    return sum(answer)