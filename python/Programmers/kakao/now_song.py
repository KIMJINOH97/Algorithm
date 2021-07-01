def solution(m, musicinfos):
    answer = []

    melody = {'C#': 'H', 'D#': 'I', 'E#': 'M', 'F#': 'J', 'G#': 'K', 'A#': 'L'}

    def clock_to_num(str1):
        hour, minute = str1.split(':')
        return int(hour)*60 + int(minute)

    def change_song(str1):
        for key in melody:
            str1 = str1.replace(key, melody[key])
        return str1

    m = change_song(m)

    for music in musicinfos:
        start, end, song, content = music.split(',')
        start, end = clock_to_num(start), clock_to_num(end)
        total_len = end-start  # 곡 길이
        content = change_song(content)

        l_song = len(content)
        really_song = content * (total_len // l_song) + \
            content[:total_len % l_song]
        if really_song.find(m) >= 0:
            answer.append((song, total_len))
    if len(answer) > 0:
        answer = sorted(answer, key=lambda x: -x[1])

    return answer[0][0] if len(answer) > 0 else "(None)"
