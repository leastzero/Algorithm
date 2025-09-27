def solution(s):
    answer = []
    dic = {}

    for index, value in enumerate(s):
        if value in dic:
            answer.append(index - dic[value])
            dic[value] = index
        else:
            answer.append(-1)
            dic[value] = index
    return answer