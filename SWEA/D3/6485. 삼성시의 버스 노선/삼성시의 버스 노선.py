t = int(input())
for i in range(1, t+1):
    station = [0] * 5001
    answer = []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            station[j] += 1

    p = int(input())
    for _ in range(p):
        c = int(input())
        answer.append(station[c])

    print("#%d" % i, end=' ')
    for x in answer:
        print(x, end=' ')
    print()