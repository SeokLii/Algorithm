def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1

    people.sort(reverse=True)
    while True:
        if start > end:
            break
        if people[start] + people[end] <= limit:
            end -= 1

        answer += 1
        start += 1

    return answer