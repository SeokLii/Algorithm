## 맨 앞과 맨 뒤의 풍선은 무조건 가능하고
## i를 기점으로 앞 뒤로 자신보다 작은 값이 있다면 불가능하다.

# 1. 앞 뒤의 최소값을 계산해서 비교하게 되면 시간초과로 불가능하다.
# def solution(a):
#     answer = 0
#     Length = len(a)
#     for i in range(1, length-1):
#         for j in range()
#     for i, v in enumerate(a):
#         # 0~ i-1까지 값중 최소값이 i 보다 작고
#         # i+1에서 N까지 값중에 최소값이 i보다 작으면 불가능
#         if i == 0 or i == Length-1:
#             answer += 1
#         else:
#             if min(a[0:i]) > v or min(a[i+1:Length]) > v:
#                 answer += 1
#     return answer


# 2. Map을 만들고 각 위치에서의 최소값을 구해서 만들어 놓고 비교하여 시간을 줄인다.
# 오른쪽에서 출발해서 오른쪽에서 가질 수 있는 최소값을 구하고 왼쪽도 동일하게 진행하여 MAP을 구성한다.
def solution(a):
    # 맨 앞, 맨 뒷 풍선은 어떻게든 남길 수 있다.
    # 가운데에 있는 풍선은, 자신을 둘러싼 풍선의 최솟값보다 작다면 남을 수 있다.
    answer = 0
    Length = len(a)
    left, right = a[0], a[Length - 1]
    maps = [[0 for _ in range(Length)] for _ in range(2)]
    # 인접한 풍선 중 번호가 큰 풍선을 터트린다.
    # 왼쪽 기준으로, 번호가 작은 풍선을 남기는 경우
    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
        maps[0][i] = left
    # 오른쪽 기준으로, 번호가 작은 풍선을 남기는 경우
    for i in range(len(a) - 1, -1, -1):
        if right > a[i]:
            right = a[i]
        maps[1][i] = right
    for i in range(len(a)):
        if a[i] <= maps[0][i] or a[i] <= maps[1][i]:
            answer += 1

    return answer


# 3. 최소값을 가져야하는지 아니면 작은 값이 있다면 다 삭제해야하는지 확인해볼 필요가 있다.