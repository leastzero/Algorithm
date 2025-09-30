def solution(cards1, cards2, goal):
    answer = "Yes"
    
    for x in goal:
        if len(cards1) > 0 and x == cards1[0]:
            del cards1[0]
        elif len(cards2) > 0 and x == cards2[0]:
            del cards2[0]
        else:
            answer = "No"
    
    return answer