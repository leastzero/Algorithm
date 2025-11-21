t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))
    answer = -1
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            isDanzo = True
            danzo = num[i] * num[j]
            str_danzo = str(danzo)
            for k in range(1, len(str_danzo)):
                if str_danzo[k] < str_danzo[k-1]:
                    isDanzo = False
                    break
            if isDanzo:
                answer = max(answer, danzo)

    print("#%d %d" % (tc, answer))