s = int(input())
n = 0
m = 1
count = 0

while n + m <= s:
    n += m
    m += 1
    count += 1

print(count)