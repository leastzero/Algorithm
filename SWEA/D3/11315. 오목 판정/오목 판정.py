dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

def DFS(x, y, idx, count):
    global answer
    if count == 5:
        answer = "YES"
        return

    nx = x + dx[idx]
    ny = y + dy[idx]

    if not (0 <= nx < n and 0 <= ny < n):
        return

    if board[nx][ny] == 'o':
        if answer == "YES":
            return 
        DFS(nx, ny, idx, count+1)
    else:
        return

t = int(input())
for i in range(1, t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    answer = "NO"

    for r in range(n):
        for c in range(n):
            if board[r][c] == 'o':
                for idx in range(4):
                    DFS(r, c, idx, 1)
                    if answer == "YES":
                        break
            if answer == "YES":
                break
        if answer == "YES":
            break
                    

    print("#%d %s" % (i, answer))