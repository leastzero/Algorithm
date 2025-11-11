t = int(input())
A, B = 0, 0
for i in range(1, t+1):
    p, q, r, s, w = map(int, input().split())
    A = w * p

    if w <= r:
        B = q
    else:
        B = q + ((w-r) * s)

    print("#%d %d" % (i, min(A, B)))