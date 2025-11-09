dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(x, y):
    global count
    if x == ex and y == ey:
        count += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0

n = int(input())

board = [[0]*n for _ in range(n)]
ch = [[0]*n for _ in range(n)]
min = 21470000
max = -21470000

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] < min:
            min = tmp[j]
            sx = i
            sy = j
        if tmp[j] > max:
            max = tmp[j]
            ex = i
            ey = j
        board[i][j] = tmp[j]

ch[sx][sy] = 1
count = 0

DFS(sx, sy)
print(count)