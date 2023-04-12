# 전 행의 최대값을 선택하여 다음행의 더 큰 값을 가져가지 못할 수 있기 때문에
# 최대값을 계속 가져간다고 해서 총합이 최고점이 되지 않는다
# 이전 행 중 자신과 동일한 행을 제외한 나머지 값들 중 최대값을 더해서 메모제이션을 통해 값을 얻는다
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[len(land) - 1])