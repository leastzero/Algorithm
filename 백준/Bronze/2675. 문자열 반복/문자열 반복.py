t = int(input())
for i in range(t):
    p=""
    r, s = input().split()
    for x in s:
        for _ in range(int(r)):
            p += x
    print(p)