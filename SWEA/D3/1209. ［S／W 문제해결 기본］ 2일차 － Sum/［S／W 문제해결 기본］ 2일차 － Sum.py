for _ in range(10):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    answer = 0
    sumC, sumD = 0, 0

    for x in board:
        answer = max(answer, sum(x))

    for row in range(100):
        sumB = 0
        for col in range(100):
            sumB += board[col][row]
        answer = max(answer, sumB)

    for i in range(100):
        sumC += board[i][i]
        sumD += board[i][99-i]
    answer = max(answer, sumC, sumD)

    print("#%d %d" % (t, answer))