def solution(cacheSize, cities):
    answer = 0
    cache = []
    low_cities = []
    for city in cities: low_cities.append(city.lower())
    if cacheSize == 0: return 5*len(cities)
    for city in low_cities:
        if city in cache:
            i = cache.index(city)
            pre, post = cache[:i], cache[i+1:]
            cache = pre+post
            cache.append(city)
            answer+=1
            continue
            
        if len(cache) == cacheSize:
            cache.pop(0)
        cache.append(city)
        answer+=5
        
    return answer