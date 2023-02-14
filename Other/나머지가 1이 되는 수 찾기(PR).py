def solution(n):
    arr = []
    # 1을 제외한 약수 중 가장 작은 수
    for i in range(2, int((n - 1) ** (0.5)) + 1):
        if (n - 1) % i == 0:
            arr.append(i)

    return arr[0] if arr else n - 1