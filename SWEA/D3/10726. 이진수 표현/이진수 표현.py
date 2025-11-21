t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    answer = ''
    mask = (1 << n) - 1
    if (m & mask) == mask:
        answer = 'ON'
    else:
        answer = 'OFF'
    print("#%d %s" % (tc, answer))