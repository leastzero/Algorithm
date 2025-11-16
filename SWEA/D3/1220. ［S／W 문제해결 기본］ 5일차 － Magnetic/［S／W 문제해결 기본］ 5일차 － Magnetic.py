for i in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for j in range(n):
        state = False
        for k in range(n):
            if board[k][j] == 1:
                state = True
            elif board[k][j] == 2:
                if state == True:
                    answer += 1
                state = False

    print("#%d %d" % (i, answer))