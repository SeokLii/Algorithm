def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 첫번째 값과 마지막 값은 그대로 더해주고 그 외의 값은 두 가지 값 중 큰 값만 넣어준다
            # 메모제이션을 통해서 값을 계속 더해가면 따로 모든 케이스를 확인하지 않고도 알 수 있다.
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    return max(triangle[-1])