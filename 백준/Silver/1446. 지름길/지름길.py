import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
for i in range(d):
    graph[i].append((i+1, 1)) # i지점에서 i+1지점으로 가는 가중치 1 존재 (기본 초기화)

dist = [INF] * (d+1) # 최단거리 저장 배열 초기화

for _ in range(n):
    start, end, weight = map(int, input().split())
    if end <= d: # 목적지를 넘지 않을 때만 추가
        graph[start].append((end, weight))

hq = []
heapq.heappush(hq, (0, 0)) # 출발지 우선순위큐에 저장
dist[0] = 0

while hq:
    cur_dist, cur = heapq.heappop(hq)

    if cur_dist > dist[cur]: # 이미 처리된 노드라면 무시
        continue

    for next, distance in graph[cur]: # 지름길이 여러개일 수 있으므로 모두 계산
        cost = cur_dist + distance
        if cost < dist[next]: # 다음 지점에 저장된 최단거리보다 지금 계산한 비용이 더 짧으면
            dist[next] = cost # 갱신
            heapq.heappush(hq, (cost, next))

print(dist[d])