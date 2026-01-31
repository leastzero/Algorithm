import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dp = [1] * 10001 # 각 숫자를 만드는 합의 개수 (숫자 1만 사용해서 더하는 경우)

    for i in range(2, n+1): # 숫자 2를 더해서 만드는 경우의 수 누적
        dp[i] += dp[i-2]

    for i in range(3, n+1): # 숫자 3을 더해서 만드는 경우의 수 누적
        dp[i] += dp[i-3]
    
    print(dp[n])