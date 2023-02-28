def solution(sizes):
    sizes = [sorted(size) for size in sizes]
    return max(sizes, key = lambda x: x[0])[0] * max(sizes, key = lambda x: x[1])[1]