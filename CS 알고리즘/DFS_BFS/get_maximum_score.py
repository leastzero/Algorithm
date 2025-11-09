def DFS(L, sum, t):
    global max_score
    if t > m:
        return
    if L == n:
        if sum > max_score:
            max_score = sum
    else:
        DFS(L+1, sum + scores[L], t + times[L])
        DFS(L+1, sum, t)

if __name__ == "__main__":
    n, m = map(int, input().split())
    scores = []
    times = []
    for i in range(n):
        score, time = map(int, input().split())
        scores.append(score)
        times.append(time)
        
    max_score = 0
    DFS(0, 0, 0)
    print(max_score)