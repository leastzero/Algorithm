import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def DFS(v):
    visited[v] = True

    for x in board[v]:
        if not visited[x]:
            parent[x] = v
            DFS(x)

n = int(input())
board = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited = [False] * (n+1)
parent = [0] * (n+1)
DFS(1)

for i in range(2, n+1):
    print(parent[i])