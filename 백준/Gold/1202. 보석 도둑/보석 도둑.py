import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))

for _ in range(k):
    c = int(input())
    bags.append(c)

jewels.sort()
bags.sort()

sum = 0
temp = []

for bag in bags:
    while jewels and jewels[0][0] <= bag:
            heapq.heappush(temp, -jewels[0][1])
            heapq.heappop(jewels)

    if temp:
        sum -= heapq.heappop(temp)

print(sum)