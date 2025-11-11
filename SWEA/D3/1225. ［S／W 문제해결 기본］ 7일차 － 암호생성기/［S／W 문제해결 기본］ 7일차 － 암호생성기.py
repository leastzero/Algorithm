from collections import deque

for _ in range(10):
    t = int(input())
    Q = list(map(int, input().split()))
    Q = deque(Q)
    Flag = 0

    while Flag == 0:
        for j in range(1, 6):
            data = Q.popleft()
            if data - j <= 0:
                Q.append(0)
                Flag = 1
                break
            else:
                Q.append(data - j)

    print("#%d" % t, end=' ')
    for x in Q:
        print(x, end=' ')