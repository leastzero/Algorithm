def DFS(L, sum):
    global profit
    if L == (n + 1):
        if sum > profit:
            profit = sum
    else:
        if L + ts[L] <= n + 1:
            DFS(L+ts[L], sum + ps[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    ts = []
    ps = []
    for _ in range(n):
        t, p = map(int, input().split())
        ts.append(t)
        ps.append(p)

    profit = 0
    ts.insert(0, 0)
    ps.insert(0, 0)
    DFS(1, 0)

    print(profit)