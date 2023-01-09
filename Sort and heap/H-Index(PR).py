def solution(citations):
    length = len(citations) + 1
    citations.sort(reverse=True)
    # 정렬하면 특정 값의 앞의 모든 값들은 조건에 만족한다는 뜻이므로 특정 값의 인덱스(조건이 맞는 값들의 개수)와 값이 같거나 크면 조건 만족한다 따라서 해당 조건이 맞지 않을 때 그 이전 값의 인덱스를 리턴해주면된다. 만약 반복문을 모두 돈다면 데이터의 모든 값이 조건에 만족하므로 리스트의 길이 리턴하면 됨
    for i in range(1, length):
        if i > citations[i-1]:
            return i - 1
    return length - 1
