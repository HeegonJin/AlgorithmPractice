def solution(gems):
    gem_num = len(list(set(gems)))
    gem_dict = {}
    start_idx, end_idx = -1, -1
    Min = 1000001
    for i in range(len(gems)):
        gem = gems[i]
        gem_dict[gem] = i
        if len(gem_dict) == gem_num:
            start_idx, end_idx = (min(gem_dict.values()), max(gem_dict.values()))

            start_key = min(gem_dict.keys(), key=lambda k: gem_dict[k])
            gem_dict.pop(start_key)

            if end_idx - start_idx < Min:
                Min = end_idx - start_idx
                answer = [start_idx + 1, end_idx + 1]

    return answer