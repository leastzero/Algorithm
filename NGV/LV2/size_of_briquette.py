import sys
input = sys.stdin.readline

n = int(input())
radius = list(map(int, input().split()))
answer = 0

for i in range(2, 101):
    count = 0
    for x in radius:
        if x % i == 0:
            count += 1
    answer = max(answer, count)

print(answer)