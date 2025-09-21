def solution(x):
    answer = True
    sumx = sum(map(int, str(x)))
    if x % sumx == 0:
        answer = True
    else:
        answer = False
    return answer