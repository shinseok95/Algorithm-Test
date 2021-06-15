def solution(genres, plays):
    answer = []
    
    genre_cnt = dict()
    play_cnt = dict()
    songs = dict()
    
    for i in range(len(genres)):
        if songs.get(genres[i]) == None:
            songs[genres[i]] = [(plays[i],i)]
            genre_cnt[genres[i]] = plays[i]
            
        else:
            songs[genres[i]].append((plays[i],i))
            genre_cnt[genres[i]] += plays[i]
    
    for genre in genre_cnt.keys():
        play_cnt[genre_cnt[genre]] = genre
    
    for play in sorted(genre_cnt.values(),reverse=True):
        
        song_list = songs[play_cnt[play]]
        
        if len(song_list) == 1:
            answer.append(song_list[0][1])
        else:
            song_list.sort(key = lambda x : (-x[0],x[1]))
            answer.append(song_list[0][1])
            answer.append(song_list[1][1])
            
    return answer