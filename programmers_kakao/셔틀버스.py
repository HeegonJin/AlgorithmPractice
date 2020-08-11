def solution(n, t, m, timetable):
    waitlist = []
    for person in timetable:
        waitlist.append(int(person[:2]) * 60 + int(person[3:]))
    waitlist.sort()
    buslist = [(9 * 60 + (i) * t) for i in range(n)]

    person_idx = 0
    bus_info = []  # 각 버스에 탄 사람들을 모두 담는 리스트
    for bus_arrival in buslist:
        this_bus = []  # 이번 버스에 타는 사람 정보를 담는 리스트
        for _ in range(m):
            if person_idx >= len(waitlist):
                break
            elif waitlist[person_idx] <= bus_arrival:
                this_bus.append(waitlist[person_idx])
                person_idx += 1
            else:
                break
        bus_info.append(this_bus)

    if len(bus_info[-1]) != m:  # 막차가 만석이 아니면
        ans = buslist[-1]  # 막차 시간 맞춰서 가자
    else:  # 막차가 만석이면
        last_person = bus_info[-1][-1]  # 막차에 마지막으로 탄사람 보다 1분 일찍 가자
        ans = last_person - 1
    ans_time, ans_minute = ans // 60, ans % 60
    if ans_time < 10:
        ans_time = "0" + str(ans_time)
    if ans_minute < 10:
        ans_minute = "0" + str(ans_minute)
    answer = str(ans_time) + ":" + str(ans_minute)
    return (answer)