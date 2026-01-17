import sys
input = sys.stdin.readline

def fib(n):
    dp[1], dp[2] = 1, 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


def fibonacci(n):
    return n-2

n = int(input())
dp = [0] * (n+1)


print(fib(n), fibonacci(n))