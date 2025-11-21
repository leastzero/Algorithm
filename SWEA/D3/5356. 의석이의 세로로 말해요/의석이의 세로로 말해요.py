t = int(input())
for tc in range(1, t+1):
    board = [[''] * 15 for _ in range(5)]
    for i in range(5):
        words = input()
        for j in range(len(words)):
            board[i][j] = words[j]
    answer = ''

    for row in range(15):
        word = ''
        for col in range(5):
            if board[col][row]:
                word += board[col][row]
            else:
                word += ''
        answer += word

    print("#%d %s" % (tc, answer))