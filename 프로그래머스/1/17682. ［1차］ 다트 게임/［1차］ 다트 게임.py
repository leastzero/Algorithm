def solution(dartResult):
    scores = []
    score = ''
    
    for value in dartResult:
        if value == "S":
            scores.append(int(score) ** 1)
            score = ''
        elif value == "D":
            scores.append(int(score) ** 2)
            score = ''
        elif value == "T":
            scores.append(int(score) ** 3)
            score = ''
        elif value == "#":
            scores[-1] *= -1
        elif value == "*":
            if len(scores) == 1:
                scores[0] *= 2
            else:
                scores[-1] *= 2
                scores[-2] *= 2
        else:
            score += value

    answer = sum(scores)
    return answer