def solution(s):
    answer = True
    countp, county = 0, 0
    
    for i in s:
        if i == 'p' or i == 'P':
            countp += 1
        if i == 'y' or i == 'Y':
            county += 1

    if countp == county:
        answer = True
    else:
        answer = False
        
    return answer