import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def DFS(v):
    visited[v] = True

    for i in board[v]:
        if visited[i] == False:
            DFS(i)

n, m = map(int, input().split())
board = [[] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

count = 0
visited = [False] * (n+1)

for i in range(1, n+1):
    if visited[i] == False:
        DFS(i)
        count += 1

print(count)