def solution(keymap, targets):
    answer = []
    press = {}
    
    for value in keymap:
        for i in range(len(value)):
            if value[i] not in press:
                press[value[i]] = i+1
            else:
                if press[value[i]]-1 > i:
                    press[value[i]] = i+1
                
    for target in targets:
        sum = 0
        for x in target:
            if x in press:
                sum += press[x]
            else:
                sum = -1
                break

        answer.append(sum)
            
    return answer