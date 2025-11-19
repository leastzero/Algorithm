dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    board[n//2-1][n//2-1] = 2
    board[n//2][n//2-1] = 1
    board[n//2-1][n//2] = 1
    board[n//2][n//2] = 2

    for _ in range(m):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color

        change = []
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            while True:
                if not (0 <= nx < n and 0 <= ny < n):
                    change = []
                    break
                if board[nx][ny] == 0:
                    change = []
                    break
                if board[nx][ny] == color:
                    break
                else:
                    change.append((nx, ny))

                nx = nx + dx[j]
                ny = ny + dy[j]

            for chx, chy in change:
                if color == 1:
                    board[chx][chy] = 1
                elif color == 2:
                    board[chx][chy] = 2
    black = 0
    white = 0

    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                black += 1
            elif board[row][col] == 2:
                white += 1

    print("#%d %d %d" % (i, black, white))