t = int(input())
for i in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1

    for j in range(1, n):
        for k in range(j-1, -1, -1):
            if num[j] > num[k]:
                dp[j] = max(dp[j], dp[k])
        dp[j] += 1

    print("#%d %d" % (i, max(dp)))