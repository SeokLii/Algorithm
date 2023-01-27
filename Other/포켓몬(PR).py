def solution(nums):
    return min(len(nums)//2, len(set(nums)))

# min으로 작은 값 반환하면 되는 것을 if 문을 사용했었음
def solution(nums):
    if len(nums) // 2 == len(set(nums)):
        return len(nums) // 2
    elif len(nums) // 2 < len(set(nums)):
        return len(nums) // 2
    else:
        return len(set(nums))
