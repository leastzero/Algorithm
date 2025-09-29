def solution(a, b, n):
    answer = 0
    
    while n >= a:
        give = n // a * a
        take = n // a * b
        answer += take
        n = n - give + take
        
    return answer