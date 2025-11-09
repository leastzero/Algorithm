# 일반 풀이법
n = int(input())
apple = 0
farm = [list(map(int, input().split())) for _ in range(n)]

s = e = n // 2
for i in range(n):
    for j in range(s, e+1):
        apple += farm[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(apple)

# BFS 풀이
from collections import deque

n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
apple = 0
farm = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]

Q = deque()
ch[n//2][n//2] = 1
Q.append((n//2, n//2))
apple += farm[n//2][n//2]
L = 0

while True:
    if L == n // 2:
        break

    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                apple += farm[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1
print(apple)