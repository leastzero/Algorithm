t = int(input())
for i in range(1, t+1):
    k, n, m = map(int, input().split())
    charger_num = list(map(int, input().split()))
    answer = 0
    current = 0

    while current + k < n:
        for j in range(k, 0, -1):
            if current + j in charger_num:
                current += j
                answer += 1
                break
        else:
            answer = 0
            break

    print("#%d %d" % (i, answer))