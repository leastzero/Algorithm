def solution(n, lost, reserve):
    pure_lost = sorted(list(set(lost) - set(reserve)))
    pure_reserve = sorted(list(set(reserve) - set(lost)))
    temp_reserve = pure_reserve[:]
    answer = n - len(pure_lost)
    
    for x in pure_lost:
        if x - 1 in temp_reserve:
            answer += 1
            temp_reserve.remove(x - 1)
        elif x + 1 in temp_reserve:
            answer += 1
            temp_reserve.remove(x + 1)
            
    return answer