def solution(today, terms, privacies):
    answer = []
    today = int(today[2:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:10])

    terms_dict = dict()
    # terms parsing
    for i in terms:
        terms_dict[i[0]] = int(i[2:])

    Date = []
    # privacies parsing
    for ymd in privacies:
        Date.append(int(ymd[2:4]) * 12 * 28 + int(ymd[5:7]) * 28 + int(ymd[8:10]) + terms_dict[ymd[11]] * 28)

    for i in range(len(Date)):
        if Date[i] <= today:
            answer.append(i + 1)

    return answer