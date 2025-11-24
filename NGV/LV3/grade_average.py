import sys

n, k = map(int, input().split())
s = list(map(int, input().split()))
for _ in range(k):
    a, b = map(int, input().split())
    sum, avg = 0, 0
    for i in range(a-1, b):
        sum += s[i]
    avg = round(sum / (b-a+1), 2)
    print(f"{avg:.2f}")