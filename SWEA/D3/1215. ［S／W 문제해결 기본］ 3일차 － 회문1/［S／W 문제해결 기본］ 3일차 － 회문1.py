for t in range(1, 11):
    n = int(input())
    board = [list(input()) for _ in range(8)]
    answer = 0

    for i in range(8):
        for j in range(0, 8-n+1):
            prev = ''
            for k in range(n):
                prev += board[i][j+k]
            if prev == prev[::-1]:
                answer += 1

    for i in range(0, 8-n+1):
        for j in range(8):
            prev = ''
            for k in range(n):
                prev += board[i+k][j]
            if prev == prev[::-1]:
                answer += 1

    print("#%d %d" % (t, answer))