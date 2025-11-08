from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
for i in range(1, t+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    answer = 0

    Q = deque()

    sx = n // 2
    sy = n // 2
    ch[sx][sy] = 1
    Q.append((sx, sy, 0))

    while Q:
        tmp = Q.popleft()
        answer += board[tmp[0]][tmp[1]]

        if tmp[2] >= n // 2:
            continue

        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if 0 <= x < n and 0 <= y < n and ch[x][y] == 0:
                ch[x][y] = 1
                Q.append((x, y, tmp[2]+1))

    print("#%d %d" % (i, answer))