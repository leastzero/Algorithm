x = int(input())
n = int(input())
l = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    l[i] = a * b

if sum(l) == x:
    print("Yes")
else:
    print("No")