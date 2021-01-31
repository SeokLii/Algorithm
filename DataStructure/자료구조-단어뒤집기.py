import sys

def reverse_text(text):
    for i in text:
        for j in i:
            print(j[::-1], end=' ')
        print()

T = int(sys.stdin.readline().rstrip())
text = [sys.stdin.readline().split() for _ in range(T)]
reverse_text(text)
