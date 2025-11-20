t = int(input())
for i in range(1, t+1):
    l, u, x = map(int, input().split())
    answer = 0
    if x > u:
        answer = -1
    elif l <= x <= u:
        answer = 0
    else:
        answer = l - x

    print("#%d %d" % (i, answer))