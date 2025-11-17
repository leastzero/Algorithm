t = int(input())
for i in range(1, t+1):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    n = int(input())
    s = input()

    for j in range(h):
        for k in range(w):
            if board[j][k] == '<' or board[j][k] == '>' or board[j][k] == '^' or board[j][k] == 'v':
                x = k
                y = j

    for o in s:
        if o == 'U':
            if y-1 >= 0 and board[y-1][x] == '.':
                board[y-1][x] = '^'
                board[y][x] = '.'
                y = y-1
            else:
                board[y][x] = '^'
        elif o == 'D':
            if y+1 < h and board[y+1][x] == '.':
                board[y+1][x] = 'v'
                board[y][x] = '.'
                y = y+1
            else:
                board[y][x] = 'v'
        elif o == 'L':
            if x-1 >= 0 and board[y][x-1] == '.':
                board[y][x-1] = '<'
                board[y][x] = '.'
                x = x-1
            else:
                board[y][x] = '<'
        elif o == 'R':
            if x+1 < w and board[y][x+1] == '.':
                board[y][x+1] = '>'
                board[y][x] = '.'
                x = x+1
            else:
                board[y][x] = '>'
        elif o == 'S':
            if board[y][x] == '^':
                for j in range(y-1, -1, -1):
                    if board[j][x] == '#':
                        break
                    if board[j][x] == '*':
                        board[j][x] = '.'
                        break
            elif board[y][x] == 'v':
                for j in range(y+1, h):
                    if board[j][x] == '#':
                        break
                    if board[j][x] == '*':
                        board[j][x] = '.'
                        break
            elif board[y][x] == '>':
                for j in range(x+1, w):
                    if board[y][j] == '#':
                        break
                    if board[y][j] == '*':
                        board[y][j] = '.'
                        break
            else:
                for j in range(x-1, -1, -1):
                    if board[y][j] == '#':
                        break
                    if board[y][j] == '*':
                        board[y][j] = '.'
                        break

    print("#%d" % i, end=' ')
    for j in range(h):
        for k in range(w):
            print(board[j][k], end='')
        print()