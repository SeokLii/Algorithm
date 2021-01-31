from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9


def bfs(graph, start, visited):
    queue = deque([start])
    # deque를 사용하지 않고 리스트로 만들 수 있음
    # queue = [start]
    visited[start] = True

    while queue:
        v = queue.popleft()
        # popleft는 deque에서만 사용할 수 있는 기능
        # 리스트에서는 pop(0) 사용
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)
