def solution(m, musicinfos):
    answer = ''
    music_list = []
    time = -1
    dic = {"C#" : '1', "D#" : '2', "F#" : '3', "G#" : '4', "A#" : '5'}
    for music in musicinfos:
        music_list.append(list(music.split(',')))
    
    for key in dic:
        m = m.replace(key, dic[key])
    
    for music in music_list:
        start_time = int(music[0][:2])*60 + int(music[0][3:])
        end_time = int(music[1][:2])*60 + int(music[1][3:])
        total_time = end_time - start_time
        cmp = ""
        for key in dic:
            music[3] = music[3].replace(key, dic[key])
        if len(music[3]) > total_time:
            cmp = music[3][:total_time]
        else:
            multi =  total_time // len(music[3])
            remain = total_time % len(music[3])
            cmp = music[3] * multi
            cmp += music[3][:remain]
        
        if m in cmp:
            if total_time > time:
                time = total_time
                answer = music[2]
    if time == -1: return "(None)"
    return answer