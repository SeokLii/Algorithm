def solution(board, moves):
    answer = 0
    row = [len(board) for i in range(len(board))]

    # 인형이 담겨 있는 행의 위치를 찾는다.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and row[j] == len(board):
                row[j] = i

    stack = []
    for i in moves:
        if row[i - 1] < len(board):
            if len(stack) >= 1:
                if stack[-1] == board[row[i - 1]][i - 1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[row[i - 1]][i - 1])
            else:
                stack.append(board[row[i - 1]][i - 1])

            row[i - 1] += 1
    return answer

# 잘못된 풀이
# row의 default 값으로 0을 넣어줘서 해당 칸에 인형이 없는 경우 0번째로 저장회덩
# 값이 들어감, 기본 값으로 board의 길이를 넣어주어 해결한다.
def solution(board, moves):
    answer = 0
    row = [0 for i in range(len(board))]

    # 인형이 담겨 있는 행의 위치를 찾는다.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and row[j] == 0:
                row[j] = i

    print(row)
    stack = []
    for i in moves:
        if len(stack) >= 1:
            if stack[-1] == board[row[i - 1]][i - 1]:
                stack.pop()
                answer += 2
            else:
                stack.append(board[row[i - 1]][i - 1])
        else:
            stack.append(board[row[i - 1]][i - 1])

        row[i - 1] += 1

    return answer