def check(row):
    for i in range(row):
        if board[i] == board[row] or abs(board[i] - board[row]) == abs(i-row):
            return False
    return True

def DFS(row):
    global answer
    if row == n:
        answer += 1
        return
    for col in range(n):
        board[row] = col
        if check(row):
            DFS(row+1)

t = int(input())
for i in range(1, t+1):
    n = int(input())
    board = [0] * n
    answer = 0

    DFS(0)

    print("#%d %d" % (i, answer))