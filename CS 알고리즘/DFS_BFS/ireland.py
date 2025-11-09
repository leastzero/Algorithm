dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]

# DFS 풀이
def DFS(x, y):
    global count
    count += 1
    board[x][y] = 0

    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            count = 0
            DFS(i, j)
            res.append(count)

print(len(res))


#BFS 풀이
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
count = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            count += 1
print(count)