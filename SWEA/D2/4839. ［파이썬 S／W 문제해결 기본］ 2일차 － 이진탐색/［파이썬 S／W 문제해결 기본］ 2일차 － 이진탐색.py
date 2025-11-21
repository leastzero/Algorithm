t = int(input())
for tc in range(1, t+1):
    p, pa, pb = map(int, input().split())
    lt, rt = 1, p
    a, b = 0, 0

    while lt <= rt:
        a += 1
        mid = (lt + rt) // 2
        if mid == pa:
            break
        elif pa < mid:
            rt = mid
        else:
            lt = mid

    lt, rt = 1, p
    while lt <= rt:
        b += 1
        mid = (lt + rt) // 2
        if mid == pb:
            break
        elif pb < mid:
            rt = mid
        else:
            lt = mid

    if a > b:
        answer = 'B'
    elif a < b:
        answer = 'A'
    else:
        answer = 0

    print("#%d %s" % (tc, answer))