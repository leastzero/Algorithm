t = int(input())

for _ in range(t):
    n = int(input())
    dic = {}
    for _ in range(n):
        s, l = input().split()
        dic[s] = int(l)
    print(max(dic, key=dic.get))