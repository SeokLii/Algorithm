def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        if answer == False:
            break;
        for j in range(len(phone_book)):
            if i != j:
                if phone_book[i].find(phone_book[j]) == 0:
                    answer = False

    return answer