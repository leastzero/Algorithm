def solution(N, stages):
    answer = []
    dic_fail = {}
    index = 0
    value = 0
    attend_people = len(stages)
    
    for i in range(1, N + 1):
        fail_people = stages.count(i)
        index = i
        if attend_people == 0:
            value = 0
        else:
            value = fail_people / attend_people
        attend_people -= fail_people
        dic_fail[index] = value
        
    sorted_fail = sorted(dic_fail.items(), key=lambda item: item[1], reverse=True)
    answer = [key for key, value in sorted_fail]
    
    return answer