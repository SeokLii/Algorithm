def solution(arr1, arr2):
    answer = []

    # 1. arr1의 열의 길이 만큼 arr2의 행의 길이 만큼 곱이 이루어져야함
    # 2. 1 step이 arr2의 열의 길이만큼 반복되어야함
    for i in range(len(arr1)):  # arr1의 열의 길이
        P = []
        for j in range(len(arr2[0])):  # arr2의 열의 길이
            T = 0
            for k in range(len(arr2)):  # arr2의 행의 길이
                T += arr1[i][k] * arr2[k][j]
            P.append(T)
        answer.append(P)

    return answer