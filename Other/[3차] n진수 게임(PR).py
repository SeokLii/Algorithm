def solution(n, t, m, p):
    answer = ''

    A = '01'
    for i in range(2, 100000):
        a = ''
        while i:
            if i % n >= 10:
                a += chr(i % n + 55)
            else:
                a += str(i % n)
            i = i // n
        A += a[::-1]

    for i in range(p - 1, len(A), m):
        if len(answer) == t:
            break
        answer += A[i]
    return answer

