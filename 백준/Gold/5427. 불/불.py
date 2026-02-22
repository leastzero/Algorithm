import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]

    sang_dist = [[-1] * w for _ in range(h)]
    fire_dist = [[-1] * w for _ in range(h)]

    sang_Q = deque()
    fire_Q = deque()

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                sang_dist[i][j] = 0
                sang_Q.append((i, j))
            elif board[i][j] == '*':
                fire_dist[i][j] = 0
                fire_Q.append((i, j))

    while fire_Q:
        x, y = fire_Q.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < h and 0 <= yy < w and board[xx][yy] != '#' and fire_dist[xx][yy] == -1:
                fire_dist[xx][yy] = fire_dist[x][y] + 1
                fire_Q.append((xx, yy))

    answer = 0
    isEscaped = False
    
    while sang_Q:
        x, y = sang_Q.popleft()

        if x == 0 or y == 0 or x == h - 1 or y == w - 1:
            isEscaped = True
            answer = sang_dist[x][y] + 1
            break

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < h and 0 <= yy < w:
                if board[xx][yy] == '.' and sang_dist[xx][yy] == -1:
                    next_time = sang_dist[x][y] + 1
                    if fire_dist[xx][yy] == -1 or fire_dist[xx][yy] > next_time:
                        sang_dist[xx][yy] = next_time
                        sang_Q.append((xx, yy))

    if isEscaped:
        print(answer)
    else:
        print("IMPOSSIBLE")