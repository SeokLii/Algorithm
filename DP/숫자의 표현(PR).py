def solution(n):
    answer = 1

    for i in range(1, n // 2 + 1):
        a = 0
        sub = 0
        while True:
            sub += i + a
            if sub >= n:
                if sub == n:
                    answer += 1
                break
            a += 1
    return answer

# 잘못된 풀이
# DP 알고리즘으로 규칙을 찾으려고 했지만, 실패한 케이스
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

# 규칙을 통한 풀이
# 다른 사람의 풀이
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])