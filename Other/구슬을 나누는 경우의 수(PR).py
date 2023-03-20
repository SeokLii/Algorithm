from itertools import combinations

def solution(balls, share):
    balls_list = [1 for i in range(balls)]
    return len(list(combinations(balls_list, share)))