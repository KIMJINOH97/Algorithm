from collections import deque


def solution(cache_size, cities):
    answer = 0
    if cache_size == 0:
        return len(cities)*5
    cache = []
    cities = list(map(lambda x: x.lower(), cities))
    for city in cities:
        l_cache = len(cache)
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if l_cache >= cache_size:
                cache.pop(0)
            cache.append(city)
            answer += 5

    return answer
