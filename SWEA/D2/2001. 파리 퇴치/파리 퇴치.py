t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    for j in range(n-m+1):
        for k in range(n-m+1):
            sum = 0
            for row in range(j, j+m):
                for col in range(k, k+m):
                    sum += board[row][col]
            res = max(res, sum)
    print("#%d %d" % (i, res))