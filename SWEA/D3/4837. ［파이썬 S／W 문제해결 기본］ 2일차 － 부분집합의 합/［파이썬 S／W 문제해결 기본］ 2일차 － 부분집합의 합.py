def DFS(L, count, sum):
    global answer
    if sum > k or count > n or (12 - L + count) < n:
        return 
    if L == 12:
        if count == n and sum == k:
            answer += 1
            return
    if count < n:
        DFS(L+1, count+1, sum+num[L])
    DFS(L+1, count, sum)

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    answer = 0
    num = list(range(1, 13))
    DFS(0, 0, 0)

    print("#%d %d" % (tc, answer))