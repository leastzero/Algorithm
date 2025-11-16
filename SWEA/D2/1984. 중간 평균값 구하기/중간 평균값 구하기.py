t = int(input())
for i in range(1, t+1):
    num = list(map(int, input().split()))
    average = 0
    num.sort()
    average_num = num[1:-1]
    average = round((sum(average_num) / (len(num)-2)))

    print("#%d %d" % (i, average))