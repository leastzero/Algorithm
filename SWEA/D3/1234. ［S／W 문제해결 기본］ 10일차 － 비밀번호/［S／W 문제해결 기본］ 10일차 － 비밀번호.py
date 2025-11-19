for i in range(1, 11):
    n, num = input().split()
    n = int(n)

    while True:
        changed = False
        current_len = len(num)
        for j in range(current_len-1):
            if num[j] == num[j+1]:
                num = num[:j] + num[j+2:]
                changed = True
                break

        if not changed:
            break

    print("#%d %d" % (i, int(num)))