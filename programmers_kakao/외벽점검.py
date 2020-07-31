from itertools import permutations


def solution(n, weak, dist):
    weak_num = len(weak)
    weak_extend = [(i + n) for i in weak]
    weak.extend(weak_extend)

    weak_list = []
    for i in range(len(weak) - weak_num):
        weak_list.append(weak[i:i + weak_num])

    friends_list = (list(permutations(dist)))
    Min = float('inf')
    success = False
    for weaks in weak_list:
        for friends in friends_list:
            friend_idx = 0  # 첫번째 친구
            start_idx = 0  # 첫번째 약점
            weak_idx = 0  # 첫번째 약점
            used = 1  # 한번 사용
            while (1):
                if friend_idx >= len(friends) or weak_idx >= len(weaks):  # 인덱스 초과 막기
                    break
                if weaks[weak_idx] - weaks[start_idx] <= friends[friend_idx]:  # 구간 커버 여부 확인
                    if weaks[weak_idx] == weaks[-1]:  # 취약 지점 전부 점검 성공
                        success = True
                        break
                    weak_idx += 1
                else:
                    start_idx = weak_idx
                    used += 1
                    friend_idx += 1

            if used < Min:
                Min = used
    if success == False:
        return -1
    answer = Min
    return answer