import sys

computer = int(sys.stdin.readline())
network = int(sys.stdin.readline())

link = [list(map(int, sys.stdin.readline().split())) for _ in range(network)]
visited = [0 for _ in range(computer+1)]

stack = []
stack.append(1)
visited[1] = 1
result = 0
print(link)

while stack:
    X = stack.pop()
    print('stack : ', stack)
    print('visited : ', visited)
    for i in link:
        print('stack : ', stack)
        if X == i[0] and visited[i[1]] == 0:
            stack.append(i[1])
            result += 1
            visited[i[1]] = 1

print(result)