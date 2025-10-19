def solution(lottos, win_nums):
    answer = []
    winnings = []
    winning = 0
    eraser = lottos.count(0)
    
    for x in lottos:
        if x in win_nums:
            winning += 1
            
    winnings.append(winning + eraser)
    winnings.append(winning)
    
    for x in winnings:
        if x == 6:
            answer.append(1)
        elif x == 5:
            answer.append(2)
        elif x == 4:
            answer.append(3)
        elif x == 3:
            answer.append(4)
        elif x == 2:
            answer.append(5)
        else:
            answer.append(6)
            
    return answer