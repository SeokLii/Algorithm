import sys

tree = {}
length = 0
while True:
    n = sys.stdin.readline().rstrip()
    if not n:
        break
    tree.setdefault(n, 0)
    tree[n] += 1
    length += 1

for i in sorted(tree.keys()):
    print('%s %.4f' %(i, ((tree[i] / length) * 100)))