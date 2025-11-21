t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    answer = []
    for i in range(1, n+1):
        if i not in num:
            answer.append(i)
    answer.sort()
    print("#%d" % tc, end=' ')
    for x in answer:
        print(x, end=' ')
    print()