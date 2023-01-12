def solution(number, k):
    num_list = list(map(int, number))
    answer = ''
    startIndex = 0

    # k(제거할 수 있는 최대 수) + 1 간격 만큼 number와 비교하며 최대값을 찾아나가기
    while k > 0:
        sub_list = num_list[startIndex:startIndex + k + 1]
        MAX = max(sub_list)
        MaxIndex = sub_list.index(MAX)

        # 최대값 넣어주기
        answer += str(MAX)
        # 다음 탐색을 위해 startIndex 값을 최대값 다음 인덱스로 변경
        startIndex += MaxIndex + 1
        # 최대 값 이전의 삭제한 앞자리 수만큼 빼주기
        k -= MaxIndex

        if len(num_list[startIndex:]) == k:
            return answer

        # 삭제할 수 있는 개수가 없고 탐색하지 않은 number가 남아있다면 합침
        elif startIndex < len(number) and k == 0:
            answer += ''.join(list(map(str, num_list[startIndex:])))

    return answer