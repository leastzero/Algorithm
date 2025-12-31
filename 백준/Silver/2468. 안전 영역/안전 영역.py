import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(x, y, d):
    visited[x][y] = True

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and board[xx][yy] >= d:
            DFS(xx, yy, d)
    

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

area = []

for i in range(1, 101):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and board[j][k] >= i:
                DFS(j, k, i)
                count += 1
    area.append(count)

print(max(area))