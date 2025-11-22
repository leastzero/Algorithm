def solution(clothes):
    answer = 1
    dic = {}
    for x in clothes:
        if x[1] in dic:
            dic[x[1]] += 1
        else:
            dic[x[1]] = 1
    for key, value in dic.items():
        answer *= (value + 1)
    answer = answer - 1
    return answer