t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = n // 10
    answer = 0
    dp = [0] * 31
    dp[1] = 1
    dp[2] = 3

    for i in range(3, m+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]

    print("#%d %d" % (tc, dp[m]))