def solution(numbers):
    numbers.sort()
    if numbers[0] < 0 and numbers[1] < 0:
        if numbers[0] * numbers[1] >= numbers[-1] * numbers[-2]:
            return numbers[0] * numbers[1]
        else:
            return numbers[-1] * numbers[-2]
    else:
        return numbers[-1] * numbers[-2]