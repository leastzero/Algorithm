k, n, m = map(int, input().split())
answer = 0

if (k * n) > m:
    answer = (k * n) - m

print(answer)