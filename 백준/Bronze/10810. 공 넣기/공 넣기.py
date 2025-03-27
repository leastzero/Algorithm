n, m = map(int, input().split())
a=[0]*(n+2)
for _ in range(m):
    i, j, k = map(int, input().split())
    for p in range(i, j+1):
        a[p] = k

for i in range(n):
    print(a[i+1], end=" ")