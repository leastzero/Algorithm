dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())
for i in range(1, t+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    x, y = 0, 0
    direction = 0

    for j in range(1, n*n+1):
        arr[x][y] = j

        xx = x + dx[direction]
        yy = y + dy[direction]

        if xx < 0 or xx >= n or yy < 0 or yy >= n or arr[xx][yy] != 0:
            direction = (direction + 1) % 4
            xx = x + dx[direction]
            yy = y + dy[direction]

        x, y = xx, yy

    print("#%d" % i)
    for x in arr:
        print(*(x))