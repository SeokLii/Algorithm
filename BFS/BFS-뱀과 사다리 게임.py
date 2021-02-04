import sys
# from collections import deque : Queue 를 만들때 사용하는 라이브러리
# 1. 변수 = deque 선언이 필요
# 2. 추가할때는 리스트와 같이 append()를 사용
# 3. 삭제할때 deque 에서 지원하는 popleft()를 사용할 수 있다.
# 4. popleft() == pop(0), 작성자는 deque 사용을 원하지 않고 리스트로 해결하기를 원하기 때문에 pop(0)을 사용할 예정

N, M = map(int, sys.stdin.readline().split())  # N(사다리수), M(뱀의수)

visited = [ -1 for _ in range(101)]
# visited == distance
# 1. 해당 인덱스를 지나갔는지의 유무 측정
# 2. 해당 인덱스까지 오는데 걸린 거리를 측정

model = [*range(101)] # *range(x) => 0~x까지 수를 1씩 늘려나가는 방법
# 해당 문제에서 제시하는 MAP
# 그래프, 타일 등 문제에서 제시한 범위를 시각화 한 것
# 어떻게 설정하는지가 시간복잡도를 결정할 수 있는 가장 큰 관건

for i in range(N+M):
    X, Y = map(int, sys.stdin.readline().split())
    model[X] = Y

Queue = []
Queue.append(1)
visited[1] = 0
# 1. 가장 먼저 큐를 만들어 준다.
# 2. 큐에 처음 값을 넣어준다.
# 3. 그리고 처음 들어가는 부분에 대해서 방문에 대한 처리를 해준다.

# 이 문제가 Queue 를 사용하는 BFS 로 풀 수 있는 이유는 Queue 를 이용해서 방문했던 곳에 다시 방문하지 않기 위함이다.
# 주사위 만큼의 수를 지속적으로 반복해서 수를 늘려가야한다는 핵심

while True:
    if visited[100] != -1:  # 끝지점에 도달했다면 끝내야 한다.
        break
    X = Queue.pop(0)
    for i in range(1, 7):  # 주사위는 1~6
        Y = X+i
        if Y <= 100:
            Y = model[Y]  # 사다리, 뱀을 이용해서 변경해줘야하기 때문이다.
            # 사다리, 뱀이 있는 지역에 도착했을 경우 해당 값으로 교체해줘야한다.
            if visited[Y] == -1 or visited[Y] > visited[X] + 1:
                # 1. 방문하지 않은 경우이거나 => 방문하지 않았으면 지금 도착한 방법의 비용으로 값에 넣어준다.
                # 2. 방문했었다면, X의 인덱스에서 Y의 인덱스에 한번의 기회로(+1로) 도착했을때,
                # Y의 값이 크다면 == Y로 왔던 기존의 방법이 지금 도착한 방법보다 더 많은 비용이 들었다면 최소값으로 바꿔줘야한다.
                visited[Y] = visited[X] + 1
                Queue.append(Y)  # 방문하지 않은 곳만 살펴봐야지, 모든 경우의 수를 살펴보게 되면 많은 시간이 들어간다.
                # 1. 방문 안했던 곳
                # 2. 방문 했지만 더 적은 비용으로 찾은 곳만 살펴볼 수 있도록 Q에 넣는다.


print(visited[100])