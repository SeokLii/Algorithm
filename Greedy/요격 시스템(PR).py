def solution(targets):
    # 구간 문제 (단속 카메라와 동일한 문제)
    # 기준의 끝 값과 다른 구간의 앞 값을 비교하는 알고리즘
    # 비교하여 기준 값이 크면 포함되므로, default[1] <= x[1][0] (개구간이라 <=) 이면 기준 변경

    # 핵심 코드 targets.sort(key=lambda x: x[1])
    # 앞이 아닌 끝을 기준으로 정렬해야 한다.
    # 기준 구간이 길고 다른 구간들이 짧을 경우, 기준에 적합하여 포함되더라도 짧은 구간들은 서로 포함되지 않을 수 있다.
    # 끝을 기준으로 정렬하면 끝 값을 순서에 따라 진행하여, 짧은 구간들이 다른 구간에 포함되지 않기 때문에 끝 값을 기준으로 정렬해야 한다.
    # 오류 케이스  [[-7,0], [-6,-4], [-5,-3], [-3,-1], [-1,4], [1,2], [3,4]]
    # 정답 4, 오답 3

    answer, point = 1, 0
    targets.sort(key=lambda x: x[1])

    for i in range(1, len(targets)):
        if targets[point][1] <= targets[i][0]:
            point = i
            answer += 1

    return answer