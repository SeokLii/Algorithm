def solution(lines):
    answer = 0
    lines.sort(key=lambda x: x[0])

    for i in range(len(lines) - 1):
        if lines[i][1] - lines[i + 1][0] > 0:
            answer += lines[i][1] - lines[i + 1][0]

    print(lines)
    return answer