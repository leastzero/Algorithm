import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
words = list(map(str, sys.stdin.readline().split()))

words.sort()

vowles = {'a', 'e', 'i', 'o', 'u'}
answer = []

all_combi = combinations(words, L)

for combo in all_combi:
    v_count = 0
    c_count = 0

    for char in combo:
        if char in vowles:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        answer.append(''.join(combo))

print(*answer, sep='\n')