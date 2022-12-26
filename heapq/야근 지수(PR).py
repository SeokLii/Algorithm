# heapq 이용해서 풀기 (최대 최소값 문제)
# 배운 부분: 따로 heap 설정한 리스트에 접근하여 값을 빼는 것이 아닌 값을 빼서 계산하고 다시 넣는 과정으로 진행
from heapq import *

def solution(n, works):
    if sum(works) <= n:
        return 0

    answer = 0
    works = [-i for i in works]
    heapify(works)
    for _ in range(n):
        A = heappop(works)
        A += 1
        heappush(works, A)

    for i in works:
        answer += i ** 2
    return answer



# 잘못된 풀이
# 계속해서 1을 빼 나가야하지만, 다른 값도 조정이 되기 때문에 문제가 됨
# [1, 7, 8, 2] n= 3
# [1, 6, 6, 2] 가 되어야 함
# 근데 계산 식은 [4 4 4 5]로 계산하게 되어 있음, 다른 업무로 값을 이동할 수 없기 때문에 잘못된 풀이
def solution(n, works):
    answer = 0
    SumWorks = sum(works)
    # n이 남아있는 일보다 많거나 같으면 0 반환
    if SumWorks <= n:
        return 0
    else:
        # 값이 클수록 제곱근의 수가 커지므로 전체적으로 낮은 값을 갖는 것이 최적의 해
        # 전체 일의 양에서 퇴근까지 남은 시간을 빼고 일의 길이만큼 나눠서 가진다
        # 나머지가 있는 경우 나머지 수 만큼 나눠 가진 일에 +1하여 계산한다.
        x = (SumWorks - n) // len(works)
        y = (SumWorks - n) % len(works)
        print(x, y, 1 // 10, 1 % 10, 0 ** 2)
        answer += x ** 2 * (len(works) - y)
        answer += (x + 1) ** 2 * (y)
        return answer

    43333928
