import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [0] * (k+1) # 각 금액을 만들 수 있는 경우의 수 저장
dp[0] = 1 # 0원을 만들 수 있는 경우: 아무 동전도 선택하지 않음 (1가지)

for _ in range(n):
    coin = int(input())
    coins.append(coin)

for c in coins:
    for i in range(c, k+1):
        dp[i] = dp[i] + dp[i-c]

print(dp[k])