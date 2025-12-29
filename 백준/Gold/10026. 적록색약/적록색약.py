import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(x, y, color):
    visited[x][y] = True

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and board[xx][yy] == color:
            DFS(xx, yy, color)

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
person1, person2 = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            DFS(i, j, board[i][j])
            person1 += 1

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            DFS(i, j, board[i][j])
            person2 += 1

print(person1, end = ' ')
print(person2)