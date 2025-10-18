from itertools import combinations
import math

def solution(nums):
    answer = 0
    combi = [sum(c) for c in combinations(nums, 3)]
    
    for value in combi:
        isPrime = True
        for i in range(2, int(math.sqrt(value))+1):
            if value % i == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1
    return answer