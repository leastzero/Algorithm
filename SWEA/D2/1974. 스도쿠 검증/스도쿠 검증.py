t = int(input())

for i in range(1, t+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    answer = 0

    for x in board:
        for j in range(1, 10):
            if x.count(j) != 1:
                answer = 1
                break

    for j in range(9):
        num = []
        for k in range(9):
            num.append(board[k][j])
        for l in range(1, 10):
            if num.count(l) != 1:
                answer = 1
                break

    is_valid = True

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            num = []
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    num.append(board[r][c])

            for j in range(1, 10):
                if num.count(j) != 1:
                    is_valid = False
                    break
            
            if not is_valid:
                break

        if not is_valid:
            break
    
    if is_valid and answer == 0:
        print("#%d %d" % (i, 1))
    else:
        print("#%d %d" % (i, 0))