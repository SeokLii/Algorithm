def stack(order, amount):
    result = []
    for i in range(amount):
        if order[i][0] == 'push':
            result.append(order[i][1])

        elif order[i][0] == 'pop':
            if len(result) == 0:
                print('-1')
            else:
                print(result.pop())

        elif order[i][0] == 'size':
            print(len(result))

        elif order[i][0] == 'empty':
            if len(result) == 0:
                print('1')
            else:
                print('0')

        elif order[i][0] == 'top':
            if len(result) == 0:
                print('-1')
            else:
                print(result[len(result)-1])

N = int(input()) # sys.stdin.readline().rstrip()
order_list = [input().split() for _ in range(N)]
stack(order_list, N)