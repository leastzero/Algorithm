import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
K = int(input()) # 시작 정점

graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1) # 최단 경로 저장 (초기값은 무한대)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 정점 u에서 v로 가는 가중치 w (여러 개 간선 존재 O)
    
pq = []
heapq.heappush(pq, (0, K)) # (거리, 정점) 우선순위큐에 삽입 (순서 주의, 거리 기준으로 자동 정렬)
dist[K] = 0 # 시작점 자신 0 출력

while pq:
    cur_dist, cur = heapq.heappop(pq) # 현재까지 가장 최단 거리 정점 꺼내기

    if dist[cur] < cur_dist: # 현재 거리보다 더 최단 거리가 있으면 컷
        continue

    for next, weight in graph[cur]: # 인접 노드의 정점, 가중치 확인
        if cur_dist + weight < dist[next]: # 인접 노드에 저장된 최단 거리보다 짧으면
            dist[next] = cur_dist + weight # 최단 거리 갱신
            heapq.heappush(pq, (cur_dist + weight, next))

for i in range(1, V+1): # 출력
    print(dist[i] if dist[i] != INF else "INF")