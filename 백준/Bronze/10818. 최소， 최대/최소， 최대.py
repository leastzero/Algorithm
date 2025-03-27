n = int(input())
a = list(map(int, input().split()))

a.sort()
print(a[0])
print(a[n-1])