def DFS(x, cnt):
    global answer

    visited[x] = 1
    for i in board[x]:
        if visited[i] == 0:
            visited[i] = 1
            DFS(i, cnt+1)
    visited[x] = 0

    if cnt > answer:
        answer = cnt

t = int(input())
for i in range(1, t+1):
    answer = 0
    n, m = map(int, input().split())
    board = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        board[x].append(y)
        board[y].append(x)

    for j in range(1, n+1):
        visited = [0 for _ in range(n+1)]
        DFS(j, 1)

    print("#%d %d" % (i, answer))