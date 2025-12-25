import sys
sys.setrecursionlimit(10000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(y, x):
    board[y][x] = 0

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < m and 0 <= yy < n and board[yy][xx] == 1:
            DFS(yy, xx)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                DFS(i, j)
                count += 1

    print(count)