from collections import deque

def solution(order):
    answer = 0
    order = [0] + order
    # 굳이 box를 만들 필요가 없다고 생각함
    box = deque([i+1 for i in range(len(order))])
    stack = deque()
    for i in range(1, len(order)):
        if order[i] > order[i-1]:
            while True:
                if order[i] == box[0]:
                    answer += 1
                    box.popleft()
                    break
                else:
                    stack.append(box[0])
                    box.popleft()
        else:
            if order[i] == stack[-1]:
                answer += 1
                stack.pop()
            else:
                break

    return answer


# 잘못된 풀이
def solution(order):
    answer = 0
    box = [i + 1 for i in range(len(order))]
    stack = []
    for i in order:
        if len(box) == 0:
            if i == stack[-1]:
                answer += 1
                stack.pop()
            else:
                break
        else:
            while len(box) != 0:
                if i == box[0]:
                    answer += 1
                    box.pop(0)
                    break
                else:
                    stack.append(box[0])
                    box.pop(0)

    return answer