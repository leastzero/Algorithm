def solution(answers):
    result = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    
    for index, answer in enumerate(answers):
        if answer == person1[index % len(person1)]:
            scores[0] += 1
        if answer == person2[index % len(person2)]:
            scores[1] += 1
        if answer == person3[index % len(person3)]:
            scores[2] += 1
            
    for index, score in enumerate(scores):
        if score == max(scores):
            result.append(index+1)
            
    return result