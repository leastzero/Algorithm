import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())
answer = 1
p %= 1000000007

while n > 0:
    if n % 2 == 1:
        answer = (answer * p) % 1000000007
    p = (p * p) % 1000000007
    n //= 2

result = (answer * k) % 1000000007
print(result)