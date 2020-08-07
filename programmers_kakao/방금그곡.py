def solution(m, musicinfos):
    global_playlist = {}
    for radio_play in musicinfos:  # 전처리
        radio_data = radio_play.split(",")
        song_name, song_melody = radio_data[2], radio_data[3]  # 음악 제목, 음악 악보
        # A#, C#, D#, F#, G# -> 소문자로 다 변경
        song_melody = song_melody.replace("A#", "a")
        song_melody = song_melody.replace("C#", "c")
        song_melody = song_melody.replace("D#", "d")
        song_melody = song_melody.replace("F#", "f")
        song_melody = song_melody.replace("G#", "g")
        hour_difference = int(radio_data[1][:2]) - int(radio_data[0][:2])
        minute_difference = int(radio_data[1][3:]) - int(radio_data[0][3:])
        play_duration = hour_difference * 60 + minute_difference  # 음악 재생시간
        play_times, play_leftover = play_duration // len(song_melody), play_duration % len(song_melody)
        what_radio_played = song_melody * play_times + song_melody[:play_leftover]
        global_playlist[song_name] = what_radio_played

    result_candidate = []
    m = m.replace("A#", "a")
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")

    for key, value in global_playlist.items():
        if m in value:
            result_candidate.append(value)

    if result_candidate == []:  # 조건에 검색되는 것 없음
        return "(None)"

    result = max(result_candidate, key=len)  # 가장 길이가 긴거, 디폴트로 맨앞에꺼 가져옴
    # https://docs.python.org/ko/3/library/functions.html#max
    for key, value in global_playlist.items():
        if value == result:
            return key