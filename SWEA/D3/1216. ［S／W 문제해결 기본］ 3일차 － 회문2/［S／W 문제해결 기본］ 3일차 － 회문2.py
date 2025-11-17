for _ in range(1, 11):
    t = int(input())
    board1 = [list(input()) for _ in range(100)]
    board2 = list(map(list, zip(*board1)))
    answer = 0

    for i in range(100):
        for j in range(100):
            for k in range(j+1, 101):
                s1 = board1[i][j:k]
                s2 = board2[i][j:k]
                if s1 == s1[::-1]:
                    answer = max(answer, len(s1))
                if s2 == s2[::-1]:
                    answer = max(answer, len(s2))

    print("#%d %d" % (t, answer))