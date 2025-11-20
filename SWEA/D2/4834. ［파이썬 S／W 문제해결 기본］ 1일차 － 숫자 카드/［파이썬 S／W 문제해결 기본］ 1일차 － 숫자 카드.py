t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = input()
    dic = {}
    a = sorted(a)
    for x in a:
        x = int(x)
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1

    max_count, max_num = 0, 0
    for key, value in dic.items():
        if value >= max_count:
            max_count = value
            max_num = key

    print("#%d %d %d" % (i, max_num, max_count))