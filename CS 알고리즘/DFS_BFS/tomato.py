from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]

Q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j))

while Q:
    tmp = Q.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x < n and 0 <= y < m and board[x][y] == 0:
            board[x][y] = 1
            Q.append((x, y))
            ch[x][y] = ch[tmp[0]][tmp[1]] + 1
flag = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(n):
        for j in range(m):
            if ch[i][j] > result:
                result = ch[i][j]
    print(result)
else:
    print(-1)