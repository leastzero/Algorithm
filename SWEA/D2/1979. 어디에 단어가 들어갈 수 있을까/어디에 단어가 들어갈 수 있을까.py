t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for j in range(n):
        count = 0
        for l in range(n):
            if board[j][l] == 1:
                count += 1
            else:
                if count == k:
                    answer += 1
                count = 0
        if count == k:
            answer += 1

    for j in range(n):
        count = 0
        for l in range(n):
            if board[l][j] == 1:
                count += 1
            else:
                if count == k:
                    answer += 1
                count = 0
        if count == k:
            answer += 1

    print("#%d %d" % (i, answer))