def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1

    # 약수 중 최대 값이 해당 숫자의 블록이 됨 (소수는 1)
    # 10000000 보다 큰 값은 해당 안되므로 조건 넣어줘야 효율성이 맞음
    for i in range(begin, end + 1):
        answer.append(1)
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                if (i // j) < 10000000:
                    answer[-1] = i // j
                    break
    return answer

# 잘못된 풀이
# 효율성 제약 조건을 넣지 않았음
# 약수를 큰 값부터 확인함 (반대로 설정함)
def solution(begin, end):
    answer = []
    if begin == 1:
        answer.append(0)
        begin += 1

    for i in range(begin, end + 1):
        for j in range(int(i ** 0.5), 0, -1):
            if i % j == 0:
                if j == 1:
                    answer.append(j)
                    break
                else:
                    answer.append(i // j)
                    break
    return answer

print(solution(121, 122))