a, b, c = map(int, input().split())
pay = 0
max = 0

if max < a:
    max = a
if max < b:
    max = b
if max < c:
    max = c

if a == b == c:
    pay = 10000+a*1000
elif a == b or a == c:
    pay = 1000+a*100
elif b == c:
    pay = 1000+b*100
else:
    pay = max*100

print(pay)