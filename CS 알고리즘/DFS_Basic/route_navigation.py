def DFS(v):
    global count
    if v == n:
        for x in path:
            print(x, end=' ')
        print()
        count += 1
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and check[i] == 0:
                check[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        n1, n2 = map(int, input().split())
        g[n1][n2] = 1

    count = 0
    check = [0] * (n + 1)
    check[1] = 1
    path = []
    path.append(1)
    DFS(1)

    print(count)