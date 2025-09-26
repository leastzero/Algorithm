def solution(t, p):
    answer = 0
    slice_num = len(p)
    
    for i in range(len(t) - slice_num + 1):
        if int(t[i:i+slice_num]) <= int(p):
            answer += 1
            
    return answer