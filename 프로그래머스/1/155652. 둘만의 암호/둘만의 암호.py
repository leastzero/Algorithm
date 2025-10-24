def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for x in skip:
        alpha = alpha.replace(x, '')
        
    for char in (s):
        original_index = alpha.find(char)
        change_index = (original_index + index) % len(alpha)
        answer += alpha[change_index]
        
    return answer