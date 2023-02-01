def solution(s):
    answer = 0

    x = ''
    x_count = 0
    s_count = 0
    for i in range(len(s)):
        if x_count == 0 and s_count == 0:
            x = s[i]
            x_count = 1
            answer += 1
            continue
        else:
            if x == s[i]:
                x_count += 1
            else:
                s_count += 1

        if x_count == s_count:
            x_count = 0
            s_count = 0

    return answer