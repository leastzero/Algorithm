def DFS(L, sum):
    global answer
    if sum == k:
        answer += 1
        return
    if L == n:
        return
    DFS(L+1, sum + a[L])
    DFS(L+1, sum)

t = int(input())
for i in range(1, t+1):
    answer = 0
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    DFS(0, 0)

    print("#%d %d" % (i, answer))