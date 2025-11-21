t = int(input())
for tc in range(1, t+1):
    n, q = map(int, input().split())
    num = [0] * n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            num[j-1] = i

    print("#%d" % tc, end=' ')
    for x in num:
        print(x, end=' ')
    print()