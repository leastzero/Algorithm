import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

s, e = map(int, input().split())

hq = []
heapq.heappush(hq, (0, s))
dist[s] = 0

while hq:
    cur_dist, cur = heapq.heappop(hq)

    if cur_dist > dist[cur]:
        continue

    for next, distance in graph[cur]:
        cost = cur_dist + distance

        if cost < dist[next]:
            dist[next] = cost
            heapq.heappush(hq, (cost, next))

print(dist[e])