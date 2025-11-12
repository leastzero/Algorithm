t = int(input())
for i in range(1, t+1):
    n = int(input())
    board = [list(input().split()) for _ in range(n)]
    answer = [[''] * n for _ in range(n)]

    for j in range(n):
        s = ''
        for k in range(n-1, -1, -1):
            s += board[k][j]
        answer[j][0] = s

    for j in range(n-1, -1, -1):
        s = ''
        for k in range(n-1, -1, -1):
            s += board[j][k]
        answer[n-j-1][1] = s

    for j in range(n-1, -1, -1):
        s = ''
        for k in range(n):
            s += board[k][j]
        answer[n-j-1][2] = s

    print("#%d" % i)
    for x in answer:
        print(*x)