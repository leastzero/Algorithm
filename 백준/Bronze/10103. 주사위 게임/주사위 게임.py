n = int(input())
chang = sang = 100

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        sang -= a
    elif a < b:
        chang -= b

print(chang)
print(sang)