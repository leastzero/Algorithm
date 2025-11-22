def solution(genres, plays):
    answer = []
    dic_genres = {}
    total_plays = {}
    
    for i in range(len(genres)):
        if genres[i] not in dic_genres:
            dic_genres[genres[i]] = []
        dic_genres[genres[i]].append([plays[i], i])
        total_plays[genres[i]] = total_plays.get(genres[i], 0) + plays[i]      
    
    for genre in dic_genres:
        list = dic_genres[genre]
        list.sort(key=lambda x: (-x[0], x[1]))
        dic_genres[genre] = list
    
    sort_genre = sorted(total_plays.items(), key=lambda item: item[1], reverse=True)
    
    for genre, total_count in sort_genre:
        list = dic_genres[genre]
        for i in range(min(len(list), 2)):
            answer.append(list[i][1])
    return answer