def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
            
    set_answer = list(set(answer))
    set_answer.sort()
    return set_answer