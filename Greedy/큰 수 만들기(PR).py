def solution(number, k):
    answer = [number[0]]
    for i in range(1, len(number)):
        if k == 0:
            return ''.join(answer) + number[i:]
        if answer[-1] < number[i]:
            while True:
                answer.pop()
                k -= 1
                if len(answer) == 0 or answer[-1] >= number[i] or k == 0:
                    break
            answer.append(number[i])
        else:
            answer.append(number[i])

    if k > 0:
        return ''.join(answer)[:len(answer) - k]
    else:
        return ''.join(answer)