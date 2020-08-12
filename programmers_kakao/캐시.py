def solution(cacheSize, cities):
    answer = 0
    cache = []
    LRU = []

    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city in cache:  # 캐시에 있을 때
            LRU.remove(cache.index(city))  # 인덱스 갱신
            LRU.append(cache.index(city))
            answer += 1
        else:  # 캐시에 없을 때
            if len(cache) < cacheSize:  # 캐시가 채워지지 않았을 때
                cache.append(city)
                LRU.append(cache.index(city))
            else:  # 캐시가 꽉찼을 때
                cache[LRU[0]] = city  # 가장 오래전에 참조한거 변경
                del LRU[0]
                LRU.append(cache.index(city))
            answer += 5
    return answer