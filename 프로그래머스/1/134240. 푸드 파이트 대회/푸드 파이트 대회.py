def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        repeat = food[i] // 2
        answer += str(i) * repeat
        
    reverse_answer = answer[::-1]
    answer += '0'
    answer += reverse_answer
    return answer