t = int(input())
for i in range(1, t+1):
    n, m, k = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    answer = 'Possible'

    for j in range(n):
        made = (arrive[j] // m) * k - (j+1)
        if made < 0:
            answer = 'Impossible'
            break

    print("#%d %s" % (i, answer))