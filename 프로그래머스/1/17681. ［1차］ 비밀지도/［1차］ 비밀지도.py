def solution(n, arr1, arr2):
    answer = []
    
    for x, y in zip(arr1, arr2):
        combine = x | y
        bin_secret = bin(combine)[2:].zfill(n)
        secert = ''
        
        for i in bin_secret:
            if i == '1':
                secert += '#'
            else:
                secert += ' '
        answer.append(secert)
    return answer