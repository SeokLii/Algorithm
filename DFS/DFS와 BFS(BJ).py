N, M, Start = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]

# 여기서 간선의 데이터가 숫자의 순서에 상관 없어야 한다
# [1, 4] == [4, 1]
# 따라서 m*m 행렬을 만들어서 1,4 와 4,1에 모두 값이 들어가도록 할 수 있다
# 아래 케이스는 인덱스로 새로 만들어주고 값이 들어있는지 확인 > 안좋은 예시
# 시간이 오래 걸림

#DFS
# 1. visitor 및 stack 생성
visitor = [0 for _ in range(N + 1)]
stack = [Start]
while stack:
    # 2. stack에서 값을 가져옴
    now = stack.pop()

    # 3. visitor 방문 여부 확인
    if visitor[now] != 1:
        visitor[now] = 1 # 방문 표시
        print(now, end=' ')
        # 4. 주변 값을 넣어준다.
        for i in reversed(Map):
            sub = i[:]
            if now in sub:
                sub.remove(now)
                if visitor[sub[0]] == 0:
                    stack.append(sub[0])

print()
#BFS
visitor = [0 for _ in range(N + 1)]
queue = [Start]
while queue:
    now = queue.pop(0)

    if visitor[now] != 1:
        visitor[now] = 1
        print(now, end=' ')
        for i in Map:
            sub = i[:]
            if now in sub:
                sub.remove(now)
                if visitor[sub[0]] == 0:
                    queue.append(sub[0])
