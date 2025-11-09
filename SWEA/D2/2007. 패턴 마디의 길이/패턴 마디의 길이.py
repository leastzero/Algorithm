t = int(input())
for i in range(1, t+1):
    s = input()
    answer = 0
    test = ''
    next_test = ''

    for j in range(11):
        test = s[:j]
        next_test = s[j:j*2]

        if j != 0 and test == next_test:
            answer = len(test)
            break

    print("#%d %d" % (i, answer))