def solution(s):
    answer = 0
    x = s[0]
    x_count = x_not_count = 0
    
    for i in range(len(s)):
        if x == s[i]:
            x_count += 1
        else:
            x_not_count += 1
            
        if x_count == x_not_count:
            answer += 1
            if i + 1 < len(s):
                x = s[i+1]
                x_count = x_not_count = 0
            else:
                break
            
    if x_count != x_not_count:
        answer += 1
        
    return answer