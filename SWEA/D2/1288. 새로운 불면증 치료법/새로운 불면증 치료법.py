t = int(input())
for i in range(1, t+1):
    n = int(input())
    num = []
    answer = 1
    j = 1

    while len(num) != 10:
        s = str(n*j)
        for x in s:
            if x not in num:
                num.append(x)
        answer = j * n
        j += 1

    print("#%d %d" % (i, answer))