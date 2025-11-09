def DFS(L, sum):
    global res
    if L == k:
        if 0 < sum <= s:
            res.add(sum)
    else:
        DFS(L+1, sum-weights[L])
        DFS(L+1, sum+weights[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    k = int(input())
    weights = list(map(int, input().split()))
    s = sum(weights)
    res = set()
    DFS(0, 0)
    answer = s - len(res)
    print(answer)