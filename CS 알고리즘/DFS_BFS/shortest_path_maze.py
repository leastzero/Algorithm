from collections import deque

maze = [list(map(int, input().split())) for _ in range(7)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ch = [[0] * 7 for _ in range(7)]

Q = deque()
maze[0][0] = 1
Q.append((0, 0))

while Q:
    tmp = Q.popleft()

    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and maze[x][y] == 0:
            maze[x][y] = 1
            ch[x][y] = ch[tmp[0]][tmp[1]] + 1
            Q.append((x, y))

if ch[6][6] == 0:
    print(-1)
else:
    print(ch[6][6])