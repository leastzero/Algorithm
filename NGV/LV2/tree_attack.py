import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for _ in range(2):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        for j in range(m):
            if board[i][j] == 1:
                board[i][j] = 0
                break

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            answer += 1
print(answer)