import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = []
for _ in range(n):
    value = int(input())
    values.append(value)

values.sort(reverse=True)
count = 0

for value in values:
    if value <= k:
        count += k // value
        k = k % value
        
print(count)