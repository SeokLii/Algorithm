def solution(triangle):
    answer = 0
    if len(triangle) == 1:
        return triangle[0]
    else:
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]

        for i in range(1, len(triangle)):
            print()
            for j in range(len(triangle[i])):
                print(j, end='')
                # if j == 0:
                #     triangle[i][j] += triangle[i-1][j]
                # elif j == len(i):
                #     triangle[i][j] += triangle[i-1][j-1]
                # else:
                #     triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    print(len(triangle))
    print(len(triangle[1]))
    return 0  # max(answer[-1])