def solution(elements):
    answer = set(elements)
    answer.add(sum(elements))
    length = len(elements)
    elements = elements * 2

    for i in range(2, length):
        for j in range(length):
            answer.add(sum(elements[j:j + i]))

    return len(answer)