import collections

def solution(X, Y):
    answer = []
    Cx = collections.Counter(X)
    Cy = collections.Counter(Y)
            
    for digit in '9876543210':
        counter_x = Cx.get(digit, 0)
        counter_y = Cy.get(digit, 0)
        
        common_count = min(counter_x, counter_y)
        
        if common_count > 0:
            answer.append(digit * common_count)
    
    answer = ''.join(answer)
    
    if not answer:
        answer = '-1'
        
    if answer[0] == '0':
        answer = '0'
        
    return answer