def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for key, value in zip(name, yearning):
        dic[key] = value
        
    for row in photo:
        sum = 0
        for item in row:
            if item in dic:
                sum += dic[item]
        answer.append(sum)
    return answer