def solution(n, m):
    gcd = 1
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break

    lcm = 0
    for i in range(max(n, m), n * m + 1):
        if i % n == 0 and i % m == 0:
            lcm = i
            break

    return [gcd, lcm]