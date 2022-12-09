def solution(s):
    # 각 케이스별로 나눌 수 있게 문자열에 불필요한 문자 제거
    a = s.replace('{{', '')
    c = a.replace('}}', '')
    d = c.replace(',', ' ')
    e = d.split('} {')

    # 중복 값이 없다는 조건은 set을 활용하라는 의미로 받아드림
    # str 값이 담긴 e 리스트를 int형 set으로 변환 (- 연산을 위해서 set 변환)
    SetList = [set(map(int, i.split())) for i in e]
    SetList.sort()  # 길이에 따라 정렬
    answer = []

    # 해당 집합보다 길이가 1 작은 집합의 차집합으로 나온 수가 순서가 됨
    # {2} > 2로 시작
    # {2, 1} > {2, 1} - {2} > {1} > 그 다음 1
    # ...
    answer += list(SetList[0])
    for i in range(len(SetList) - 1):
        answer += list(SetList[i + 1] - SetList[i])

    return answer