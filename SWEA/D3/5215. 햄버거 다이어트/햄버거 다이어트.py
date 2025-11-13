def DFS(L, score, kcal):
    global answer
    if kcal > l:
        return
    if L == n:
        answer = max(answer, score)
        return

    DFS(L+1, score + food[L][0], kcal + food[L][1])
    DFS(L+1, score, kcal)


tc = int(input())
for i in range(1, tc+1):
    n, l = map(int, input().split())
    food = []
    answer = 0
    for _ in range(n):
        t, k = map(int, input().split())
        food.append((t, k))

    DFS(0, 0, 0)
    print("#%d %d" % (i, answer))