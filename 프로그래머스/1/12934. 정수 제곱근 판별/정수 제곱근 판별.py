import math

def solution(n):
    answer = 0
    x = math.sqrt(n)
    if x == int(x):
        answer = (x + 1) * (x + 1)
    else:
        answer = -1
    return answer