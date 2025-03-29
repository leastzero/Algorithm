n = int(input())
a = list(map(int, input().split()))
a.sort()

for i in range(n):
    a[i] = a[i] / a[-1] * 100

sum = sum(a)
avg = sum / n

print(avg)