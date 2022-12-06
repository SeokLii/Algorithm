def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        for j in range(max(answer, arr[i]), answer * arr[i] + 1):
            if j%answer == 0 and j%arr[i] == 0:
                answer = j
                break
    return answer