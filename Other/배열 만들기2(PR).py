def solution(l, r):
    list2 = [0, 5, 50, 55]
    start, end = 0, 0

    for i in range(2, len(str(r))):
        for j in list2[:]:
            list2.append(5 * 10 ** i + j)

    for s in range(len(list2)):
        if list2[s] >= l:
            start = s
            break

    for e in range(len(list2) - 1, 0, -1):
        if list2[e] <= r:
            end = e
            break

    return list2[start:end + 1] if start < end + 1 else [-1]