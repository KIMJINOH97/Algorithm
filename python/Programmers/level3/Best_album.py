def solution(genres, plays):
    answer = []
    dic = {}
    genre_play = {}
    for i, g in enumerate(genres):
        if g not in dic:
            dic[g] = [[i, plays[i]]]
            genre_play[g] = plays[i]
            continue
        dic[g].append([i, plays[i]])
        genre_play[g] += plays[i]
    
    genre_play = sorted(genre_play, key = lambda x: -genre_play[x])
    
    for k in dic:
        dic[k] = sorted(dic[k], key = lambda x: -x[1])
    
    for g in genre_play:
        for i in range(len(dic[g])):
            if i == 2: break
            answer.append(dic[g][i][0])
    
    
    return answer