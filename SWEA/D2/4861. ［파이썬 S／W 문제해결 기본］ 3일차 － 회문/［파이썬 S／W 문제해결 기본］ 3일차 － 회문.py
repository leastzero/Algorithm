t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    answer = ''

    for row in range(n):
        for col in range(n-m+1):
            poly = ''
            for k in range(col, col+m):
                poly += board[row][k]
            if poly == poly[::-1]:
                answer = poly
                break

    for row in range(n):
        for col in range(n-m+1):
            poly = ''
            for k in range(col, col+m):
                poly += board[k][row]
            if poly == poly[::-1]:
                answer = poly
                break

    print("#%d %s" % (tc, answer))