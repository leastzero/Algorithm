def solution(s):
    answer = ''
    arr = s.split(' ')
    for x in arr:
        for i in range(len(x)):
            if i % 2 == 0:
                answer += x[i].upper()
            else:
                answer += x[i].lower()
        answer += ' '
    return answer[:-1]