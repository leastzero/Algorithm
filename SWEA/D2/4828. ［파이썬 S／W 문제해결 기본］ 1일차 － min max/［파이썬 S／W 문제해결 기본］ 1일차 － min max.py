t = int(input())
for i in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))

    max_num = max(num)
    min_num = min(num)
    print("#%d %d" % (i, max_num - min_num))