from collections import deque
n, k = map(int, input().split())
visit = [0 for i in range(100001)]
queue = deque()
queue.append([n, 0])
while queue:
    p, d = queue[0][0], queue[0][1]
    if p == k:
        break
    queue.popleft()
    visit[p] = 1
    if p - 1 >= 0 and visit[p - 1] == 0:
        queue.append([p - 1, d + 1])
    if p + 1 <= 100000 and visit[p + 1] == 0:
        queue.append([p + 1, d + 1])
    if p * 2 <= 100000 and visit[p * 2] == 0:
        queue.append([p * 2, d + 1])
print(queue[0][1])

## 위에는 남의 정답 아래는 내가 틀린 답
# N, K = map(int, input().split())
#
# store = [0] * (100000 + 1)
#
#
# def bfs(store, start, finish):
#     time = 0
#     v = [[start]]
#     while True:
#         time += 1
#         v_middle = []
#         for i in v[0]:
#             if store[i*2] != 0 and store[i*2] > time and i * 2 <= 100000:
#                 store[i*2] = time
#                 v_middle.append(i * 2)
#             elif store[i*2] == 0 and i * 2 <= 100000:
#                 store[i*2] = time
#                 v_middle.append(i * 2)
#
#             if store[i + 1] != 0 and store[i + 1] > time and i + 1 <= 100000:
#                 store[i + 1] = time
#                 v_middle.append(i + 1)
#             elif store[i + 1] == 0 and i + 1 <= 100000:
#                 store[i + 1] = time
#                 v_middle.append(i + 1)
#
#             if i - 1 > 0:
#                 if store[i - 1] != 0 and store[i - 1] > time:
#                     store[i - 1] = time
#                     v_middle.append(i - 1)
#                 elif store[i - 1] == 0:
#                     store[i - 1] = time
#                     v_middle.append(i - 1)
#
#             v.append(v_middle)
#             v.pop(0)
#
#         if store[finish] != 0:
#             break
#     print(time)
#
# bfs(store, N, K)