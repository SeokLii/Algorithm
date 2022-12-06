def solution(n):
    # 결국은 1로 나아가고 n에 가장 가까운 2의 제곱 수 만큼 뺀다
    # n =0이 될 때 까지 반복
    # 결국 2진법과 동일함
    return format(n, 'b').count('1')

