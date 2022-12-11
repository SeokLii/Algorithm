def solution(n, k):
    # 10진수 일 때는 바로 진행
    if k == 10:
        # count('')
        Pn = str(n).split('0')
        for _ in range(Pn.count('')):
            Pn.remove('')
    else:
        # k진수일 때 자리수 구하기
        length = 0
        k_str = []
        while k ** length <= n:
            length += 1
            k_str.append('0')

        # n을 k 진수로 표현
        for i in reversed(range(length)):
            if k ** i <= n and k ** (i + 1) > n:
                k_str[i] = str(n // k ** i)
                n = n % k ** i
        k_str.reverse()

        # 0을 구분하여 split('0')
        Pn = ''.join(k_str).split('0')
        for _ in range(Pn.count('')):
            Pn.remove('')

    # 저장된 각 수가 소수인지 판단 (약수가 1가 자기 자신인지)
    answer = 0
    for i in Pn:
        count = 0
        if i == '1':
            count += 1

        for j in range(2, int((int(i) ** 0.5)) + 1):
            if int(i) % j == 0:
                count += 1

        if count == 0:
            answer += 1

    return answer