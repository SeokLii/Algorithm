def solution(s):
    answer = []
    A = list(map(int, s.split()))
    answer.append(str(min(A)))
    answer.append(str(max(A)))

    # str(min(A) + ' ' + max(A))
    # join은 리스트의 자료형이 str이어야함
    return ' '.join(answer)