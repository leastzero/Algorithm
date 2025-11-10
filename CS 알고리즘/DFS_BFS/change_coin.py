def DFS(L, sum):
    global count
    if sum > t:
        return
    if L == k:
        if sum == t:
            count += 1
    else:
        for i in range(ns[L]+1):
            DFS(L+1, sum+(ps[L]*i))

if __name__ == "__main__":
    t = int(input())
    k = int(input())

    ps = []
    ns = []
    for _ in range(k):
        p, n = map(int, input().split())
        ps.append(p)
        ns.append(n)

    count = 0
    DFS(0, 0)
    print(count)