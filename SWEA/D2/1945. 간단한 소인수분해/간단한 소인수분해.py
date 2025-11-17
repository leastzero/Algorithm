t = int(input())
for i in range(1, t+1):
    n = int(input())
    dic = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    for index, key in enumerate(dic):
        while n % key == 0:
            n = n // key
            dic[key] += 1

    print("#%d %d %d %d %d %d" % (i, dic[2], dic[3], dic[5], dic[7], dic[11]))