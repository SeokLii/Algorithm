def merge_the_tools(string, k):
    N = len(string) // k
    P = len(string)// N

    for i in range(N):
        T = i * P
        print(''.join(list(set(string[T:T + P]))))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)