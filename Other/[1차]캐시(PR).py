from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cities = [i.upper() for i in cities]
    cache = deque([cities[0]])
    answer = 5

    for i in range(1, len(cities)):
        if cities[i] in cache:
            answer += 1
            cache.remove(cities[i])
            cache.appendleft(cities[i])
        else:
            answer += 5
            if len(cache) == cacheSize:
                cache.pop()
                cache.appendleft(cities[i])
            else:
                cache.appendleft(cities[i])

    return answer