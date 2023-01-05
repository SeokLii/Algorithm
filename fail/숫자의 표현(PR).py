def solution(n):
    answer = 0
    cnt = 1
    while True:
        if cnt == n:
            print('a', cnt)
            break
        else:
            if cnt%2 == 1:
                if n%cnt == 0:
                    print(cnt)
                    answer += 1
            else:
                if (n - cnt//2)%cnt == 0:
                    print(cnt)
                    answer += 1
            cnt += 1
    return answer