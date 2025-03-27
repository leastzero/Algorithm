a = [0] * 10
for i in range(10):
    n = int(input())
    a[i] = n % 42
    
a = set(a)
a = list(a)
print(len(a))