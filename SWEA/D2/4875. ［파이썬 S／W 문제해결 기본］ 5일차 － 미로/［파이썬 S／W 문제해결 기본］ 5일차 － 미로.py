dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global answer
    if x == ex and y == ey:
        answer = 1
        return

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] != 1 and ch[xx][yy] == 0:
            ch[xx][yy] = 1
            DFS(xx, yy)
            ch[xx][yy] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    sx, sy, ex, ey = 0, 0, 0, 0
    answer = 0
    ch = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if board[row][col] == 2:
                sx = row
                sy = col
            if board[row][col] == 3:
                ex = row
                ey = col

    ch[sx][sy] = 1
    DFS(sx, sy)

    print("#%d %d" % (tc, answer))