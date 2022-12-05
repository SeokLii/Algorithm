def solution(s):
    Stack = [0]

    for i in range(len(s)):
        if s[i] == Stack[len(Stack) - 1]:
            Stack.pop()
        else:
            Stack.append(s[i])

    return 0 if len(Stack) != 1 else 1