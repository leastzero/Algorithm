def DFS(L, sum, tsum):
    global max
    if sum + (total - tsum) < max:
        return
    if sum > c:
        return
    
    if L == n:
        if max < sum:
            max = sum
    else:
        DFS(L+1, sum + baduki[L], tsum + baduki[L])
        DFS(L+1, sum, tsum + baduki[L])

if __name__ == '__main__':
    c, n = map(int, input().split())
    baduki = [0] * n
    for i in range(n):
        baduki[i] = int(input())

    max = 0
    total = sum(baduki)
    DFS(0, 0, 0)
    print(max)