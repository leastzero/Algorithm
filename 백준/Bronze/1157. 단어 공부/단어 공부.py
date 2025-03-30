n = input()
n = n.upper()

a = [0]*26
for x in n:
    a[ord(x) - 65] += 1

res = 0
max = -2147000000
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        res = i

a.sort()
if a[-1] == a[-2]:
    print("?")
else:
    print(chr(res + 65))