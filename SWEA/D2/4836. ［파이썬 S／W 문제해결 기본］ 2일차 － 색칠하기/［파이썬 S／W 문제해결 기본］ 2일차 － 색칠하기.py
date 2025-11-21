t = int(input())
for i in range(1, t+1):
    n = int(input())
    board = [[0] * 10 for _ in range(10)]
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                board[row][col] += color

    answer = 0
    for row in range(10):
        for col in range(10):
            if board[row][col] == 3:
                answer += 1
    print("#%d %d" % (i, answer))