def solution(array):
    answer = 0
    counts = [0] * (max(array)+1)
    
    for i in array:
        counts[i] += 1
        
    if counts.count(max(counts)) > 1:
        answer = -1
    else:
        answer = counts.index(max(counts))
            
    return answer