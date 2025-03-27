n, m = map(int, input().split())
a = [0]*(n+2)

for i in range(1, n+1):
    a[i] = i

tmp = 0
for _ in range(m):
    i, j = map(int, input().split())
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

for i in range(1, n+1):
    print(a[i], end=" ")