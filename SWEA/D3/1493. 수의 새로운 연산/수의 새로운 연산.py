def get_coord(n):
    k = 2
    while True:
        current_sum = (k * (k-1)) // 2
        if n <= current_sum:
            break
        k += 1

    prev_sum = ((k-1) * (k-2)) // 2
    x = n - prev_sum
    y = k - x

    return x, y

def get_number(x, y):
    k = x + y
    prev_sum = ((k-1) * (k-2)) // 2
    return prev_sum + x

t = int(input())
for i in range(1, t+1):
    p, q = map(int, input().split())
    answer = 0

    x1, y1 = get_coord(p)
    x2, y2 = get_coord(q)

    answer = get_number(x1+x2, y1+y2)

    print("#%d %d" % (i, answer))