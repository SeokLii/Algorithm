#괄호 문제는 스택 구조로 풀이
from collections import deque


def solution(s):
    answer = 0
    deq = deque(s)

    if len(s) <= 1:
        return 0

    for _ in range(len(s)):
        deq.rotate(1)
        check = deque()
        count = 0

        for i in deq:
            if i in '[{(':
                check.appendleft(i)
            else:
                if i == ']' and len(check) > 0:
                    if '[' == check[0]:
                        check.popleft()
                        count += 1
                elif i == '}' and len(check) > 0:
                    if '{' == check[0]:
                        check.popleft()
                        count += 1
                elif i == ')' and len(check) > 0:
                    if '(' == check[0]:
                        check.popleft()
                        count += 1
                else:
                    count += 100000
                    break

        if len(check) == 0 and count == len(s) // 2:
            answer += 1

    return answer


# 오답 노트
# if in 으로 확인하는 방식에서 오류가 남 stack처럼 last in first out 방식으로 check를 구성해니까 오류가 해결됨
# def solution(s):
#     answer = 0
#     deq = deque(s)
#
#     if len(s) <= 1:
#         return 0
#
#     for _ in range(len(s)):
#         deq.rotate(1)
#         check = deque()
#         count = 0
#
#         for i in deq:
#             if i in '[{(':
#                 check.appendleft(i)
#             else:
#                 if i == ']' and len(check) > 0:
#                     if '[' in check: #오류구간
#                         check.remove('[')
#                         count += 1
#                 elif i == '}' and len(check) > 0:
#                     if '{' in check:
#                         check.remove('{')
#                         count += 1
#                 elif i == ')' and len(check) > 0:
#                     if '(' in check:
#                         check.remove('(')
#                         count += 1
#                 else:
#                     count += 100000
#                     break
#
#         if len(check) == 0 and count == len(s) // 2:
#             answer += 1
#
#     return answer