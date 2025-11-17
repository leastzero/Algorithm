t = int(input())
for i in range(1, t+1):
    money = int(input())
    dic = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}

    for index, key in enumerate(dic):
        while money - key >= 0:
            money = money - key
            dic[key] += 1

    print("#%d" % i)
    for x in dic.items():
        print(x[1], end=' ')
    print()