from collections import deque

def solution(x, y, n):
    que = deque()
    que.append([x, 0])

    while (que):
        q = que.popleft()

        if q[0] == y:
            return q[1]

        for i in ['n', '2', '3']:
            if i == 'n':
                if q[0] + n <= y:
                    que.append([q[0] + n, q[1] + 1])
            if i == '2':
                if q[0] * 2 <= y:
                    que.append([q[0] * 2, q[1] + 1])
            if i == '3':
                if q[0] * 3 <= y:
                    que.append([q[0] * 3, q[1] + 1])
    return -1