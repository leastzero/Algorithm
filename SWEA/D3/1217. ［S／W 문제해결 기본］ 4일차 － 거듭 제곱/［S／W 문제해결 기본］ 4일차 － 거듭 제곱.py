for _ in range(1, 11):
    t = int(input())
    n, m = map(int, input().split())
    answer = 1
    for _ in range(m):
        answer *= n

    print("#%d %d" % (t, answer))