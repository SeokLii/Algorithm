# 문제 1
def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += n // a * b
        n = n // a * b + n % a

    return answer

# 문제 2
def solution(s):
    answer = []
    queue = []

    for i in range(len(s)):
        if s[i] not in queue:
            answer.append(-1)
            queue += s[i]
        else:
            for j in range(len(queue) - 1, -1, -1):
                if queue[j] == s[i]:
                    answer.append(i - j)
                    queue += s[i]
                    break

    return answer