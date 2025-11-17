t = int(input())
for i in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))

    num.sort()
    print("#%d" % i, end=' ')
    for x in num:
        print(x, end=' ')
    print()