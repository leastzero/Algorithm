def solution(k, m, score):
    answer = 0
    sorted_score = sorted(score, reverse=True)
    index = m - 1
    
    while index < len(score):
        answer += sorted_score[index] * m
        index += m
        
    return answer