a=[]
for i in range(9):
    a.append(int(input()))

max = 0
idx = 0
for i in range(9):
    if a[i] > max:
        max = a[i]
        idx = i + 1

print(max)
print(idx)
