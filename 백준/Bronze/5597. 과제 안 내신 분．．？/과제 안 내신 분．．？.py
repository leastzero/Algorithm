a = [0] * 31
for _ in range(1, 29):
    n = int(input())
    a[n] = n

for i in range(1, 31):
    if a[i] == 0:
        print(i)