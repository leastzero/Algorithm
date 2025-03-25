A, B = map(int, input().split())
C = int(input())

if B + C < 60:
    B = B + C
else:
    A += (B + C) // 60
    B = (B + C) % 60

if (A >= 24):
    A = A - 24

print(A, B)