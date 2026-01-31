import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            sx = i
            sy = j
            break

visited = [([-1] * m) for _ in range(n)]
visited[sx][sy] = 0

Q = deque()
Q.append((sx, sy))

while Q:
    x, y = Q.popleft()

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m:
            if visited[xx][yy] == -1 and board[xx][yy] == 1:
                visited[xx][yy] = visited[x][y] + 1
                Q.append((xx, yy))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()