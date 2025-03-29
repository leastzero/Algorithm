n, m = map(int, input().split())
a = list(range(n+1))

for _ in range(m):
    i, j = map(int, input().split())
    for k in range((j-i+1)//2):
        a[i+k], a[j-k] = a[j-k], a[i+k]

a.pop(0)
for x in a:
    print(x, end=" ")