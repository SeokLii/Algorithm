N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for k in range(1, i+1):
        print(k, dp)
        dp[i] = max(dp[i], dp[i-k] + p[k])
# dp[n] = n 개를 사는 최대값
# dp[1] = 1개를 사는 최대값
# dp[1] = dp[1] 과 dp[0] + 1개를 뽑는 비용
# dp[2] = dp[1] 과 dp[1] + 1개를 뽑는 비용
# dp[2] = dp[2] 와 dp[0] + 2개를 뽑는 비용
# ... 이런식으로 점화식을 이어가는 방식
# 솔직히 잘 모르겟다
print(dp[i])


# 내가 햇는데 틀린답
# import sys
# N = int(sys.stdin.readline())
#
# P_List = [0] + list(map(int, sys.stdin.readline().split()))
# P_Weight = [0] # 가격 / 카드의 수 = 가중치
# result = 0
#
# for index, value in enumerate(P_List):
#     if index == 0:
#         continue
#     P_Weight.append(value/index)
#
# while True:
#     if N == 0:
#         break
#
#     MAX = max(P_Weight)  # 가중치에서 가장 큰 값
#     W_index = P_Weight.index(MAX)  # 큰 값의 인덱스 = 카드의 수
#     if N < W_index:  # 살 수 있는 카드의 수 보다 사야할 카드의 수가 더 크면 = 못 사면
#         P_Weight[W_index] = 0  # 가장 큰 값을 못사니까 계산에서 제외
#     else:  # 살 수 있으면
#         N -= W_index  # 카드의 수를 빼주고
#         result += P_List[W_index]  # 그 카드의 가격을 결과에 넣어준다.
#
#     print(P_Weight)
#
# print(result)

