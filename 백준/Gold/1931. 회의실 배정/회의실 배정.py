import sys
input = sys.stdin.readline

n = int(input())
times = []

for _ in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

count = 0
times.sort(key=lambda x: (x[1], x[0]))
finish = 0

for s, e in times:
    if s >= finish:
        count += 1
        finish = e

print(count)