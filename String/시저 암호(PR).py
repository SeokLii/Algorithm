def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if 97 <= ord(i) <= 122:
                result = ord(i) + n
                if result > 122:
                    answer += chr(result - 26)
                else:
                    answer += chr(result)
            else:
                result = ord(i) + n
                if result > 90:
                    answer += chr(result - 26)
                else:
                    answer += chr(result)

    return answer