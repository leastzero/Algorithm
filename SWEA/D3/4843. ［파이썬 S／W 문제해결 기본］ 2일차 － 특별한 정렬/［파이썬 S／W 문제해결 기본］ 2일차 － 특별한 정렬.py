t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()
    lt, rt = 0, n-1
    answer = []

    while lt <= rt:
        answer.append(num[rt])
        answer.append(num[lt])
        lt += 1
        rt -= 1
    print("#%d" % tc, end=' ')
    for i in range(10):
        print(answer[i], end=' ')
    print()