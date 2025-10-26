def solution(survey, choices):
    answer = ''
    choice_scores = {1: 3, 2: 2, 3: 1, 5: 1, 6: 2, 7: 3}
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(choices)):
        if choices[i] <= 3:
            scores[survey[i][0]] += choice_scores[choices[i]]
        elif choices[i] >= 5:
            scores[survey[i][1]] += choice_scores[choices[i]]
    
    if scores['R'] >= scores['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if scores['C'] >= scores['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if scores['J'] >= scores['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if scores['A'] >= scores['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer