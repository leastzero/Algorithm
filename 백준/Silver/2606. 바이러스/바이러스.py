import sys
input = sys.stdin.readline

def DFS(v):
    global count
    count += 1
    visited[v] = 1

    for node in graph[v]:
        if visited[node] == 1:
            continue
        DFS(node)


n = int(input())
pair = int(input())
graph = [[] for _ in range(n+1)]
count = 0

for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

DFS(1)
print(count-1)