def minion_game(string):
    Stuart = 0
    Kevin = 0

    #slicing의 end이전까지의 값만가져옴
    #stirng[1:2] 이면 첫번째 인덱스만 나옴
    for i in range(len(string)):
        if string[i] in "AEIOU":
            Kevin += len(string[i:])
        else:
            Stuart += len(string[i:])

    if Stuart == Kevin:
        print("Draw")
    elif Stuart > Kevin:
        print("Stuart", Stuart)
    else:
        print("Kevin", Kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)