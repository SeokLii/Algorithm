def solution(s, skip, index):
    answer = ''
    # 97 ~ 122
    skip = [ord(i) for i in skip]

    for i in s:
        loop = index
        ask = ord(i)
        while loop != 0:
            ask += 1
            if ask > 122:
                ask = (ask % 123) + 97

            if ask not in skip:
                loop -= 1

        answer += chr(ask)

    return answer